import pytest

pytestmark = [
    pytest.mark.requires_salt_modules("servicenow.example_function"),
]


@pytest.fixture
def servicenow(modules):
    return modules.servicenow


def test_replace_this_this_with_something_meaningful(servicenow):
    echo_str = "Echoed!"
    res = servicenow.example_function(echo_str)
    assert res == echo_str
