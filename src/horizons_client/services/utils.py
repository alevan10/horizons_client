import os
import re
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import List

import pandas as pd

from horizons_client.services.response_object import ResponseObject


class CsvFileWriter(object):
    def __init__(self, csv_data: str):
        self.csv_data = csv_data
        self.file = NamedTemporaryFile(mode="w", delete=False)

    def __enter__(self):
        self.file.write(self.csv_data)
        self.file.flush()
        self.file.close()
        return Path(self.file.name)

    def __exit__(self, *args, **kwargs):
        os.remove(Path(self.file.name))


def deserialize_ephem_data(raw_data: str) -> List[ResponseObject]:
    header_pattern = re.compile("(Date[\s\S]*?)\*")
    body_pattern = re.compile("\$\$SOE([\s\S]*?)\$\$EOE")
    header_match = header_pattern.findall(raw_data)
    body_match: List[str] = body_pattern.findall(raw_data)
    assert len(body_match) == 1 and len(header_match) == 1
    full_data = header_match[0].replace(" ", "") + body_match[0].replace("n.a.", "")
    with CsvFileWriter(full_data) as tmp_file_path:
        df: pd.DataFrame = pd.read_csv(Path(tmp_file_path), sep=",", index_col=False)
    records = df.dropna(axis=1).to_dict(orient="records")
    return [ResponseObject(response_dict=record) for record in records]
