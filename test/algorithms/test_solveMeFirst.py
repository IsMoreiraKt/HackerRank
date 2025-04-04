from algorithms.solveMeFirst import solveMeFirst
import pytest

@pytest.mark.parametrize("a, b, res", [
    (1, 2, 3),
    (5, 5, 10),
    (-2, 5, 3),
    (100, -50, 50),
    (1556, 2554, 4110),
])
def test_solveMeFirst(a, b, res):
    assert solveMeFirst(a, b) == res

