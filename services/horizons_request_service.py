import csv
import os
import re
from io import StringIO
from pathlib import Path
from tempfile import TemporaryFile, NamedTemporaryFile

import pandas as pd
from typing import List, Dict
from aiohttp import ClientSession

from services.request_objects import BaseRequestObject
from services.utils import CsvFileWriter

HORIZONS_BASE_URL = os.environ.get("HORIZONS_BASE_URL", "https://ssd.jpl.nasa.gov/api/horizons.api")


def cleanse_column_name(old_column_names: List[str]) -> Dict[str, str]:
    new_column_names = [column_name.split("_")[0].lower() for column_name in old_column_names]
    return {o: n for o, n in zip(old_column_names, new_column_names)}


def retrieve_ephem_data(raw_data: str) -> pd.DataFrame:
    header_pattern = re.compile("(Date[\s\S]*?)\*")
    body_pattern = re.compile("\$\$SOE([\s\S]*?)\$\$EOE")
    header_match = header_pattern.findall(raw_data)
    body_match: List[str] = body_pattern.findall(raw_data)
    assert len(body_match) == 1 and len(header_match) == 1
    full_data = header_match[0].replace(" ", "") + body_match[0].replace(" ", "").replace("n.a.", "")
    with CsvFileWriter(full_data) as tmp_file_path:
        df: pd.DataFrame = pd.read_csv(Path(tmp_file_path), sep=",")
    return df.rename(columns=cleanse_column_name(list(df.columns)))


class HorizonsRequestService(object):
    base_params = [
        ('format', 'json'),
        ('MAKE_EPHEM', 'YES'),
        ('EPHEM_TYPE', 'OBSERVER'),
        ('ANG_FORMAT', 'DEG'),
        ('CSV_FORMAT', 'YES')
    ]

    def __init__(self, request_objects: List[BaseRequestObject] = None):
        if request_objects is None:
            request_objects = []
        self._request_objects: List[BaseRequestObject] = request_objects

    async def make_request(self) -> pd.DataFrame:
        request_params = [*self.base_params]
        for obj in self._request_objects:
            request_params.append(obj.generate_request_param())
        async with ClientSession() as session:
            async with session.request(method='GET', url=HORIZONS_BASE_URL, params=request_params) as resp:
                assert resp.ok
                response_data = await resp.json()
                result = response_data.get('result')
                assert result
                return retrieve_ephem_data(result)

    def add_parameter(self, request_obj: BaseRequestObject):
        self._request_objects.append(request_obj)
