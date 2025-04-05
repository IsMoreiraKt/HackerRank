from algorithms.diagonalDifference import diagonalDifference
import pytest

@pytest.mark.parametrize("ar, result", [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0),
    ([[9, 8, 7], [6, 5, 4], [3, 2, 1]], 0),
    ([[15, 33, 1], [26, 84, 12], [7, 55, 45]], 52),
    ([[-99, 84, 42], [12, 25, 33], [32, 88, 98]], 75),
    ([[57, 84, 2], [1, 885, 4], [231, 87, 4]], 172),
])
def test_diagonalDifference(ar: list, result: int) -> None:
    assert diagonalDifference(ar) == result

