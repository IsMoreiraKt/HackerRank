from algorithms.compareTriplets import compareTriplets
import pytest

@pytest.mark.parametrize("a, b, result", [
    ([5, 6, 7],    [3, 6, 10],  [1, 1]),
    ([17, 28, 30], [99, 16, 8], [2, 1]),
    ([5, 5, 5],    [0, 0, 0],   [3, 0]),
    ([0, 0, 0],    [5, 5, 5],   [0, 3]),
])
def test_compareTriplets(a: list, b: list, result: list) -> None:
    assert compareTriplets(a, b) == result

