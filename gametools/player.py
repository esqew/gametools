from typing import Optional
from .cards import CardCollection
from .bank import PlayerBank

class Player:
    name: str
    bank: Optional[PlayerBank]

    def __init__(self, name: str) -> None:
        self.name = name
        self.bank = None
        return
    
    def give(self, amount: float | int, to: 'Player') -> None:
        """
        Transfer an amount from this `Player`'s bank to another `Player`'s bank.

        Args:
            amount (float | int): The amount to transfer.
            to (Player): The target `Player` to receive the funds.

        Raises:
            ValueError: If either player does not have a bank.
        """
        if self.bank is None:
            raise ValueError(f"Player {self.name} does not have a bank")
        if to.bank is None:
            raise ValueError(f"Player {to.name} does not have a bank")
        
        return self.bank.give(amount=amount, to=to.bank)

class CardPlayer(Player):
    hand: CardCollection = CardCollection()

    def __init__(self, name: str, starting_balance: float = 100.0) -> None:
        super().__init__(name=name)
        self.bank = PlayerBank(starting_balance=starting_balance)
        return