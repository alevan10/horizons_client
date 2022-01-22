from parser import ParserError  # pylint: disable=deprecated-module
from unittest import mock

import pytest

from horizons_client.entities.enums import ResponseOptions
from horizons_client.services.response_object import (
    DATETIME_PARSE_MESSAGE,
    ResponseObject,
)


@pytest.fixture
def example_horizons_date():
    yield "2022-Jan-17 09:41:58.197"


# pylint: disable=redefined-outer-name
def test_instantiate_with_date(example_horizons_date):
    obj = ResponseObject({ResponseOptions.DATE: example_horizons_date})
    assert obj
    date = obj.date
    assert date.month == 1
    assert date.day == 17
    assert date.year == 2022
    assert date.hour == 9
    assert date.minute == 41
    assert date.second == 58
    assert date.microsecond == 197000


@pytest.mark.parametrize("bad_date", ["none", None, 13, True, {"some": "stuff"}])
def test_instantiate_with_bad_date(bad_date):
    with mock.patch("horizons_client.services.response_object.logger") as mock_logger:
        imput_dict = {ResponseOptions.DATE: bad_date}
        with pytest.raises((ParserError, ValueError, TypeError)):
            ResponseObject(imput_dict)
            assert mock_logger.assert_called_with(
                DATETIME_PARSE_MESSAGE.format(bad_date), extra=imput_dict
            )
