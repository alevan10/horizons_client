from datetime import datetime
from typing import Any, Dict, List
from unittest import mock

import pytest
from asynctest import CoroutineMock
from freezegun import freeze_time

from horizons_client.entities.enums import ResponseOptions
from horizons_client.services.response_object import ResponseObject


@pytest.fixture
def good_columns() -> List[str]:
    yield [ResponseOptions.DATE, "col_2", "col_3"]


@pytest.fixture
def bad_columns() -> List[str]:
    yield ["unnamed_1", "", "unnamed_2"]


@pytest.fixture
# pylint: disable=redefined-outer-name
def test_columns(good_columns, bad_columns) -> List[str]:
    yield [*good_columns, *bad_columns]


class MockResponseObject(ResponseObject):
    def __init__(self, response_dict: Dict[str, Any]):
        self.col_2 = response_dict.pop("col_2")
        self.col_3 = response_dict.pop("col_3")
        self.others = response_dict
        super().__init__(response_dict)


@freeze_time("2022-01-01")
@pytest.fixture
def test_rows():
    row_1 = [f"{datetime.now()}", "row_1", "row_1", "", "", ""]
    row_2 = [f"{datetime.now()}", "row_2", "row_2", "", "", ""]
    row_3 = [f"{datetime.now()}", "row_3", "row_3", "", "", ""]
    yield [row_1, row_2, row_3]


@pytest.fixture
def generate_headers():
    def _format_headers(columns: List[str]) -> str:
        return f"****************\n{','.join(columns)}\n****************\n"

    yield _format_headers


@pytest.fixture
def generate_body_data():
    def _format_ephem_data(rows: List[List[str]]) -> str:
        formatted_rows = [",".join(row) for row in rows]
        data = "\n".join(formatted_rows)
        return f"$$SOE{data}\n$$EOE"

    yield _format_ephem_data


@pytest.fixture
# pylint: disable=redefined-outer-name
def test_raw_data(test_columns, test_rows, generate_headers, generate_body_data):
    headers = generate_headers(test_columns)
    body = generate_body_data(test_rows)
    yield headers + body


@pytest.fixture
def use_mock_response_object():
    with mock.patch("horizons_client.services.utils.ResponseObject") as response_object:
        response_object.side_effect = MockResponseObject
        yield response_object


@pytest.fixture
def patch_client_session(get_horizons_response):
    default_response = get_horizons_response()

    def _generator(return_data=default_response):
        with mock.patch(
            "horizons_client.services.horizons_request_service.aiohttp.ClientSession.get"
        ) as mock_get:
            mock_get.return_value.__aenter__.return_value.json = CoroutineMock(
                side_effect={"result": return_data}
            )
            return mock_get

    yield _generator
