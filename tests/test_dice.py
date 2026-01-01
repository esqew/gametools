import gametools.dice as dice
import pytest

@pytest.fixture
def die() -> dice.StandardDie:
    return dice.StandardDie(sides=6)

class TestDie:
    def test_roll(self, die: dice.StandardDie) -> None:
        result = die.roll()
        assert 1 <= result <= 6, f"roll_d6() returned {result}, which is out of range"
        assert result == die.value, f"die.value {die.value} does not match roll result {result}"