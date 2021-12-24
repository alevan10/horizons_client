import json
from typing import Dict
from unittest import mock

import pytest
from pathlib import Path


@pytest.fixture
def repo_root_dir() -> Path:
    yield Path(__file__).resolve().parent.parent


@pytest.fixture
def test_dir(repo_root_dir) -> Path:
    yield Path.joinpath(repo_root_dir, 'tests')


@pytest.fixture
def testdata_dir(test_dir) -> Path:
    yield Path.joinpath(test_dir, 'testdata')


@pytest.fixture
def base_horizons_request(testdata_dir) -> str:
    with open(Path.joinpath(testdata_dir, 'horizons_request.txt')) as request_file:
        request = request_file.readlines()
        request_file.flush()
    request = "".join(request)
    yield request


@pytest.fixture
def json_request(base_horizons_request):
    yield base_horizons_request + "format=json"


@pytest.fixture
def text_request(base_horizons_request):
    yield base_horizons_request + "format=text"


@pytest.fixture
def get_horizons_response(testdata_dir):
    def _get_response(format: str='json') -> str:
        with open(Path.joinpath(testdata_dir, f"{format}_horizons_response.txt")) as response_file:
            response = response_file.readlines()
            response_file.flush()
        response = "".join(response)
        return response
    yield _get_response


@pytest.fixture
def json_response(get_horizons_response) -> Dict[str, str]:
    yield json.loads(get_horizons_response(format="json"))


@pytest.fixture
def text_response(get_horizons_response) -> str:
    yield get_horizons_response(format="text")


@pytest.fixture
def mock_json_response(get_horizons_response):
    with mock.patch("services.horizons_request.service.aiohttp.get") as mock_get:
        mock_get.return_value = get_horizons_response(format="json")
        yield


@pytest.fixture
def mock_text_response(get_horizons_response):
    with mock.patch("services.horizons_request.service.aiohttp.get") as mock_get:
        mock_get.return_value = get_horizons_response(format="text")
        yield
