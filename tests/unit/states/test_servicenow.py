import pytest
import salt.modules.test as testmod
import saltext.servicenow.modules.servicenow_mod as servicenow_module
import saltext.servicenow.states.servicenow_mod as servicenow_state


@pytest.fixture
def configure_loader_modules():
    return {
        servicenow_module: {
            "__salt__": {
                "test.echo": testmod.echo,
            },
        },
        servicenow_state: {
            "__salt__": {
                "servicenow.example_function": servicenow_module.example_function,
            },
        },
    }


def test_replace_this_this_with_something_meaningful():
    echo_str = "Echoed!"
    expected = {
        "name": echo_str,
        "changes": {},
        "result": True,
        "comment": f"The 'servicenow.example_function' returned: '{echo_str}'",
    }
    assert servicenow_state.exampled(echo_str) == expected
