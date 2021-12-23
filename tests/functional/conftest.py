from datetime import datetime, timedelta

import pytest
import pytest_freezegun

from entities.enums import Planets, Observers
from services.horizons_request_service import HorizonsRequestService
from services.request_objects import StartTimeRequest, StopTimeRequest, CommandRequestObject, CenterRequestObject


@pytest.fixture
@pytest.mark.freeze_time
def generate_request_object() -> HorizonsRequestService:
    horizons = HorizonsRequestService()
    horizons.add_parameter(StartTimeRequest(value=datetime.now()))
    horizons.add_parameter(StopTimeRequest(value=datetime.now() + timedelta(days=1)))
    horizons.add_parameter(CommandRequestObject(value=Planets.VENUS))
    horizons.add_parameter(CenterRequestObject(value=Observers.SUN))
    yield horizons
