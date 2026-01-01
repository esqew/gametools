import abc
import random
from typing import Any

class Die(abc.ABC):
    @property
    @abc.abstractmethod
    def value(cls) -> Any:
        """
        The current value of the die, most often the last value rolled.
        """
        ...

    @abc.abstractmethod
    def roll(self) -> Any:
        """
        Roll the die and return the result.
        """
        ...

class StandardDie(Die):
    """
    Representation of a standard n-sided die, with whole number values between 1 and n (inclusive).
    """
    def __init__(self, sides: int = 6) -> None:
        self.sides = sides
        self._value = 1
        return

    @property
    def value(self) -> int:
        return self._value

    def roll(self) -> int:
        self._value = random.randint(1, self.sides)
        return self._value
