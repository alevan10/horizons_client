from entities.enums import APIEnum


class TestClass(APIEnum):
    attribute_1 = "1"
    attribute_2 = "2"
    attribute_3 = "3"


def test_APIEnum_to_list():
    test_attributes = ["attribute_1", "attribute_2", "attribute_3"]
    attribute_list = TestClass.to_list()
    for test_attribute in test_attributes:
        assert test_attribute in attribute_list
