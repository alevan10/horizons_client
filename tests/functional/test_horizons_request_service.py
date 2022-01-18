import pytest


@pytest.mark.asyncio
async def test_can_make_request_to_horizons(generate_request_object):
    horizons = generate_request_object
    response = await horizons.make_request()
    assert response
