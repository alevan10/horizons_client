import pytest

from horizons_client.entities.enums import Observers, Planets
from horizons_client.services.horizons_request_service import HorizonsRequestService
from horizons_client.services.request_objects import (
    CenterRequestObject,
    CommandRequestObject,
    StartTimeRequest,
    StopTimeRequest,
)


@pytest.fixture
@pytest.mark.freeze_time
def generate_request_object(start_time, end_time) -> HorizonsRequestService:
    horizons = HorizonsRequestService()
    horizons.add_parameter(StartTimeRequest(value=start_time))
    horizons.add_parameter(StopTimeRequest(value=end_time))
    horizons.add_parameter(CommandRequestObject(value=Planets.VENUS))
    horizons.add_parameter(CenterRequestObject(value=Observers.SUN))
    yield horizons
