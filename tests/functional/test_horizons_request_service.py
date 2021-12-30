import pytest


class TestHorizonsRequestService(object):

    @pytest.mark.asyncio
    async def test_can_make_request_to_horizons(self, generate_request_object):
        horizons = generate_request_object
        response = await horizons.make_request()
        assert response


