from algorithms.plusMinus import plusMinus
from _pytest.capture import CaptureFixture, CaptureResult
import pytest


@pytest.mark.parametrize("a, result", [
  (
    [
      1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17,
      -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30, -31, -32,
      -33, -34
    ],
    "0.287671\n0.465753\n0.246575\n"
  ),
  (
    [
      1, 2, 3, 4, 5, 6, 7,
      0, 0, 0, 0, 0,
      -1, -2, -3, -4, -5, -6, -7
    ],
    "0.368421\n0.368421\n0.263157\n"
  ),
  (
    [
      1, 2, 3, 4, 5, 6, 7, 8,
      0, 0, 0,
      -1, -2, -3, -4, -5, -6, -7, -8, -9
    ],
    "0.400000\n0.450000\n0.150000\n"
  ),
  (
    [
      1, 2, 3, 4, 5, 6,
      0, 0, 0, 0, 0, 0, 0, 0,
      -1, -2, -3, -4, -5, -6, -7, -8
    ],
    "0.272727\n0.363636\n0.363636\n"
  ),
  (
    [
      1, 2, 3, 4,
      0, 0, 0, 0, 0, 0,
      -1, -2, -3, -4, -5, -6, -7, -8, -9
    ],
    "0.210526\n0.473684\n0.315789\n"
  )
])
def test_plusMinus(a: list, result: str, capsys: CaptureFixture[str]) -> None:
  plusMinus(a)
  captured: CaptureResult[str] = capsys.readouterr()

  expected: list = list(map(float, result.strip().split("\n")))
  actual: list = list(map(float, captured.out.strip().split("\n")))

  for act, exp in zip(actual, expected):
    assert abs(act - exp) <= 1e-4, f"Expected {exp}, got {act}"
