from typing import List

import pytest

from horizons_client.services.utils import deserialize_ephem_data
from tests.unittests.conftest import MockResponseObject


class TestDeserializeEphemData(object):

    @pytest.mark.usefixtures("use_mock_response_object")
    def test_deserialize_ephem_data(self, test_raw_data, good_columns, bad_columns, test_rows):
        responses: List[MockResponseObject] = deserialize_ephem_data(test_raw_data)
        assert len(responses) == len(test_rows)
        for response, row in zip(responses, test_rows):
            for column in good_columns:
                if column != "Date":
                    assert response.__getattribute__(column) in row
                else:
                    assert response.test_date in row
            for bad_column in bad_columns:
                assert bad_column not in response.others.keys()


