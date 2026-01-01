import gametools.dice as dice
import pytest

@pytest.fixture
def die() -> dice.StandardDie:
    return dice.StandardDie(sides=6)

@pytest.fixture
def n8_die() -> dice.StandardDie:
    return dice.StandardDie(sides=8)

class TestDie:
    def test_roll(self, die: dice.StandardDie) -> None:
        result = die.roll()
        assert 1 <= result <= 6, f"roll_d6() returned {result}, which is out of range"
        assert result == die.value, f"die.value {die.value} does not match roll result {result}"

    def test_str_and_repr(self, die: dice.StandardDie, n8_die: dice.StandardDie) -> None:
        die.roll()
        n8_die.roll()

        str_value = str(die)
        assert str_value in ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"], f"Unexpected string representation: {str_value}"

        str_value = str(n8_die)
        assert str_value == f"[{n8_die.value}]", f"Unexpected string representation for n8 die: {str_value}"
        
        repr_value = repr(die)
        assert repr_value == f"StandardDie(sides=6, value={die.value})", f"Unexpected repr representation: {repr_value}"
