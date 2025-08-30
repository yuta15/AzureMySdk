import pytest

from src.resources.common.model import common_class_values as v_class
from src.resources.common.model import common_class as c_class


def test_location_values_members():
    assert v_class.LocationValues.JAPAN_EAST.value == "Japan East"
    assert v_class.LocationValues.JAPAN_WEST.value == "Japan West"

def test_location_subclass_stores_value():
    class MyLocation(c_class.Location):
        pass
    loc = MyLocation(v_class.LocationValues.JAPAN_EAST)
    assert loc.location is v_class.LocationValues.JAPAN_EAST

@pytest.mark.parametrize(
    ["value", "result"],
    [
        pytest.param(
            "test value",
            True
        ),
        pytest.param(
            " test_value",
            False
        ),
    ]
)
def test_tag_key_name_rule(value, result):
    key_name_rule = v_class.TagKeyNameRule()
    assert result == key_name_rule.is_match(value)

def test_tag_aggregate_resource():
    first_resource = c_class.TagAggregateResource([])
    second_resource = c_class.TagAggregateResource([])
    first_resource.tags.append(
        c_class.TagBase(
            tag_key="test",
            tag_value="test_value"
        )
    )
    assert first_resource.tags != second_resource.tags

def test_location_aggreate_resource():
    japan_east = v_class.LocationValues.JAPAN_EAST
    japan_west = v_class.LocationValues.JAPAN_WEST
    location1 = c_class.Location(location=japan_east)
    location2 = c_class.Location(location=japan_west)
    object1 = c_class.LocationAggregateResource(location1)
    object2 = c_class.LocationAggregateResource(location1)
    object1.location = location2
    assert object1.location != object2

def test_tag_location_aggreate_resource():
    japan_east = v_class.LocationValues.JAPAN_EAST
    japan_west = v_class.LocationValues.JAPAN_WEST
    location1 = c_class.Location(location=japan_east)
    location2 = c_class.Location(location=japan_west)
    object1 = c_class.TagLocationAggregateResource(location1, [])
    object2 = c_class.TagLocationAggregateResource(location1, [])
    object1.location = location2
    assert object1.location != object2
    object2.location = location2
    object1.tags.append(c_class.TagBase(
            tag_key="test",
            tag_value="test_value"
        )
    )
    assert object1.location != object2