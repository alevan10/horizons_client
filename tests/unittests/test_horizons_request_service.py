import pytest

from horizons_client.entities.enums import Observers, Planets
from horizons_client.services.horizons_request_service import (
    HORIZONS_BASE_URL,
    HorizonsRequestService,
)
from horizons_client.services.request_objects import (
    CenterRequestObject,
    CommandRequestObject,
    StartTimeRequest,
    StopTimeRequest,
)


@pytest.fixture
def request_objects(start_time, end_time):
    command = CommandRequestObject(value=Planets.EARTH)
    center = CenterRequestObject(value=Observers.SUN)
    start = StartTimeRequest(value=start_time)
    stop = StopTimeRequest(value=end_time)
    yield [command, center, start, stop]


@pytest.mark.asyncio
async def test_make_request(patch_client_session, request_objects):
    session = patch_client_session()
    horizons_svc = HorizonsRequestService(request_objects)
    response = await horizons_svc.make_request()

    assert len(response) == 1
    assert session.assert_called()
    expected_params = [
        *HorizonsRequestService.base_params,
        ("COMMAND", "'399'"),
        ("CENTER", "'@10'"),
        request_objects[2].generate_request_param(),
        request_objects[3].generate_request_param(),
    ]
    assert session.assert_called_once_with(
        url=HORIZONS_BASE_URL, params=expected_params
    )
