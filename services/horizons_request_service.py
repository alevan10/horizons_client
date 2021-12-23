import os
from typing import List
from aiohttp import ClientSession

from services.request_objects import BaseRequestObject

HORIZONS_BASE_URL = os.environ.get("HORIZONS_BASE_URL", "https://ssd.jpl.nasa.gov/api/horizons.api")


class HorizonsRequestService(object):
    base_url = f"{HORIZONS_BASE_URL}" \
               f"?format=json" \
               f"&MAKE_EPHEM=YES" \
               f"&EPHEM_TYPE=OBSERVER" \
               f"&ANG_FORMAT=DEG" \
               f"&CSV_FORMAT=YES"

    def __init__(self, request_objects: List[BaseRequestObject]=None):
        if request_objects is None:
            request_objects = []
        self._request_objects: List[BaseRequestObject] = request_objects

    async def make_request(self) -> str:
        request_url = self.base_url
        for obj in self._request_objects:
            request_url += obj.generate_request_param()
        async with ClientSession() as session:
            async with session.get(request_url) as resp:
                assert resp.ok
                response_data = await resp.text()
                return response_data

    def add_parameter(self, request_obj: BaseRequestObject):
        self._request_objects.append(request_obj)

