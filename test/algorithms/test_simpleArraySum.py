from algorithms.simpleArraySum import simpleArraySum
import pytest

@pytest.mark.parametrize("ar, result", [
    ([3], 3),
    ([7, 2], 9),
    ([1, 4, 9], 14),
    ([8, 5, 3, 6], 22),
    ([10, 20, 30, -50], 10),
    ([12, 7, 5, 3, 9, 1, 6], 43),
])
def test_simpleArraySum(ar: list, result: int) -> None:
    assert simpleArraySum(ar) == result

