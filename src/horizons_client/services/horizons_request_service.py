import logging
import os
from typing import List

from aiohttp import ClientSession

from horizons_client.services.request_objects import BaseRequestObject
from horizons_client.services.response_object import ResponseObject
from horizons_client.services.utils import deserialize_ephem_data

HORIZONS_BASE_URL = os.environ.get(
    "HORIZONS_BASE_URL", "https://ssd.jpl.nasa.gov/api/horizons.api"
)
logger = logging.getLogger(__name__)


class HorizonsRequestService(object):
    base_params = [
        ("format", "json"),
        ("MAKE_EPHEM", "YES"),
        ("EPHEM_TYPE", "OBSERVER"),
        ("ANG_FORMAT", "DEG"),
        ("CSV_FORMAT", "YES"),
    ]

    def __init__(self, request_objects: List[BaseRequestObject] = None):
        if request_objects is None:
            request_objects = []
        self._request_objects: List[BaseRequestObject] = request_objects

    async def make_request(self) -> List[ResponseObject]:
        request_params = [*self.base_params]
        for obj in self._request_objects:
            request_params.append(obj.generate_request_param())
        logger.debug("Request params", extra={"params": request_params})
        async with ClientSession() as session:
            async with session.get(
                url=HORIZONS_BASE_URL, params=request_params
            ) as resp:
                assert resp.ok
                response_data = await resp.json()
                result = response_data.get("result")
                assert result
                return deserialize_ephem_data(result)

    def add_parameter(self, request_obj: BaseRequestObject):
        self._request_objects.append(request_obj)
