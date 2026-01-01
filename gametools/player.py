from typing import Optional
from .cards import CardCollection
from .bank import PlayerBank

class Player:
    name: str

class CardPlayer(Player):
    hand: CardCollection
    bank: Optional[PlayerBank]