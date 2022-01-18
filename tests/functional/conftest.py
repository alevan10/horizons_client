from datetime import datetime, timedelta

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
def generate_request_object() -> HorizonsRequestService:
    horizons = HorizonsRequestService()
    horizons.add_parameter(StartTimeRequest(value=datetime.now()))
    horizons.add_parameter(StopTimeRequest(value=datetime.now() + timedelta(days=1)))
    horizons.add_parameter(CommandRequestObject(value=Planets.VENUS))
    horizons.add_parameter(CenterRequestObject(value=Observers.SUN))
    yield horizons
