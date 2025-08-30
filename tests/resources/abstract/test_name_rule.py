import pytest
from src.resources.abstract.model.base_class_values import NameRule


@pytest.mark.parametrize(
    ["pattern", "name", "result"],
    [
        pytest.param(
            r"^[a-z0-9]([a-z0-9-]{1,22}[a-z0-9])?$",
            "a111111111111-1111111111",
            True
            ),
        pytest.param(
            r"^[a-z0-9]([a-z0-9-]{1,22}[a-z0-9])?$",
            "a111111111111-11111111119",
            False
            ),
        pytest.param(
            r"^[a-z0-9]([a-z0-9-]{1,22}[a-z0-9])?$",
            "_111111111111-1111111111",
            False
            ),
    ]
)
def test_name_rule(pattern, name, result):
    name_rule = NameRule(pattern)
    assert result == name_rule.is_match(name)