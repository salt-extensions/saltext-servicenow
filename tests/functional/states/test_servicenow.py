import pytest

pytestmark = [
    pytest.mark.requires_salt_states("servicenow.exampled"),
]


@pytest.fixture
def servicenow(states):
    return states.servicenow


def test_replace_this_this_with_something_meaningful(servicenow):
    echo_str = "Echoed!"
    ret = servicenow.exampled(echo_str)
    assert ret.result
    assert not ret.changes
    assert echo_str in ret.comment
