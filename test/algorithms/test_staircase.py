from algorithms.staircase import staircase
from _pytest.capture import CaptureFixture, CaptureResult
import pytest

@pytest.mark.parametrize("ar, result", [
  (5, "    #\n   ##\n  ###\n ####\n#####\n"),
  (3, "  #\n ##\n###\n"),
  (6, "     #\n    ##\n   ###\n  ####\n #####\n######\n"),
  (1, "#\n")
])
def test_staircase(ar: int, result: str, capsys: CaptureFixture[str]) -> None:
  staircase(ar)
  captured: CaptureResult[str] = capsys.readouterr()

  assert captured.out == result
