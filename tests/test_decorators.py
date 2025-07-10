from typing import Any

import pytest

from src.decorators import log


@log()
def my_function(x: float, y: float) -> Any:
    return x / y


@pytest.mark.parametrize(
    "x, y, output",
    [
        (6, 2, "INFO: my_function ok: Inputs: 6, 2. Outputs: 3.0\n"),
        (6, 4, "INFO: my_function ok: Inputs: 6, 4. Outputs: 1.5\n"),
        (81, 9, "INFO: my_function ok: Inputs: 81, 9. Outputs: 9.0\n"),
        (17, 0, "ERROR: my_function error: division by zero. Inputs: 17, 0. Outputs: None\n"),
    ],
)
def test_log(capsys, x, y, output):
    my_function(x, y)
    captured = capsys.readouterr()
    assert captured.out == output
