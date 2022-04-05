from datetime import datetime

import pytest

from horizons_client.entities.exceptions import RequestException
from horizons_client.services.request_objects import (
    BaseRequestObject,
    StartTimeRequest,
    StopTimeRequest,
)


@pytest.fixture
def fake_request_class():
    class FakeRequestObject(BaseRequestObject):

        name = "Fake-Object"

    yield FakeRequestObject


# pylint: disable=redefined-outer-name
def test_base_request_object(fake_request_class):
    fake_object = fake_request_class(value="parakeet value")
    assert fake_object.name == "Fake-Object"
    assert fake_object.value == "parakeet value"
    assert fake_object.generate_request_param() == ("FAKE-OBJECT", "'parakeet value'")


def test_base_request_fails_if_lacking_name():
    with pytest.raises(NotImplementedError):
        bad_object = BaseRequestObject(value="please fail")
        assert not bad_object


@pytest.mark.parametrize("time_object", [StartTimeRequest, StopTimeRequest])
def test_time_objects(time_object):
    test_time_obj = time_object(
        value=datetime(year=2021, month=11, day=28, hour=9, minute=30, second=0)
    )
    assert test_time_obj.generate_request_param() == (
        test_time_obj.name.upper(),
        "'2021-Nov-28 09:30:00.000000'",
    )


@pytest.mark.usefixtures("freezer")
@pytest.mark.parametrize("time_object", [StartTimeRequest, StopTimeRequest])
def test_time_objects_only_accept_datetime_objects(time_object):
    test_time_obj = time_object(datetime.now())
    assert test_time_obj
    assert test_time_obj.value == datetime.now()

    with pytest.raises(RequestException):
        bad_time_obj = time_object(value="please fail")
        assert not bad_time_obj
