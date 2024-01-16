import pytest
from mlproject.utils import TwoNumbers


@pytest.fixture(scope="session")
def zero_zero():
    return TwoNumbers(0, 0)
