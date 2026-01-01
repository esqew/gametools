from enum import Enum
import random

class CoinResult(Enum):
    """
    Enum representing the possible outcomes of a coin flip.
    """
    HEADS = 1
    TAILS = 2

class Coin:
    """
    A class representing a coin that can be flipped to produce a random result.
    """

    def __init__(self, value: CoinResult = CoinResult.HEADS) -> None:
        """
        Initialize the coin with a default value.

        Args:
            value (CoinResult): The initial value of the coin. Defaults to HEADS.
        """
        self.value: CoinResult = value
        return

    def flip(self) -> CoinResult:
        """
        Flip the coin to randomly set its value to HEADS or TAILS.

        Returns:
            CoinResult: The result of the coin flip.
        """
        self.value = random.choice(list(CoinResult))
        return self.value

    def __repr__(self):
        """
        Return a string representation of the Coin object.

        Returns:
            str: A string representation of the coin's current value.
        """
        return f"Coin(value={self.value})"