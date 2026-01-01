from collections import UserList
import random

class Card:
    """
    Represents a generic card with a suit, rank, and sort order.
    """
    suit: str
    rank: int | str
    sort_rank: int
    face_down: bool | None = True
    
    def __lt__(self, other: 'Card') -> bool:
        """
        Compares two cards based on their sort rank.

        Args:
            other (Card): The card to compare against.

        Returns:
            bool: True if this card's sort rank is less than the other card's.
        """
        if not isinstance(other, Card):
            raise TypeError("Cannot compare Card with non-Card type")
        return self.sort_rank < other.sort_rank
    
    def __eq__(self, other: 'Card') -> bool: # pyright: ignore[reportIncompatibleMethodOverride]
        """
        Checks if two cards are equal based on their rank.

        Args:
            other (Card): The card to compare against.

        Returns:
            bool: True if this card's sort rank is less than the other card's.
        """
        if not isinstance(other, Card):
            raise TypeError("Cannot compare Card with non-Card type")
        return self.sort_rank == other.sort_rank

class FrenchSuit:
    """
    Defines the suits and ranks for a standard French deck of cards.
    """
    SUITS: list[str] = ['❤', '♦', '♣', '♠']
    RANKS: list[str] = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

class PlayingCard(Card, FrenchSuit):
    """
    Represents a playing card with a specific suit and rank.
    """
    def __init__(self, suit, rank):
        """
        Initializes a playing card with the given suit and rank.

        Args:
            suit (str): The suit of the card; checked against gametools.cards.FrenchSuit.SUITS
            rank (str): The rank of the card; checked against gametools.cards.FrenchSuit.RANKS

        Raises:
            ValueError: If the suit or rank is invalid.
        """
        super().__init__()
        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit: {suit}")
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank: {rank}")
        self.suit = suit
        self.rank = rank
        self.sort_rank = self.RANKS.index(rank)

    def __str__(self):
        """
        Returns a string representation of the card.
        """
        return f"[{self.suit}{self.rank}]"

    def __repr__(self):
        """
        Returns a detailed string representation of the card.
        """
        return f"PlayingCard(suit='{self.suit}', rank='{self.rank}')"

class CardCollection(UserList[Card]):
    """
    Represents a collection of cards with additional functionality.
    """
    @property
    def cards(self):
        """
        Returns a string representation of all cards in the collection.
        """
        return ', '.join(str(card) for card in self.data)
    
    def append(self, item: Card) -> None:
        """
        Adds a card to the collection.

        Args:
            item (Card): The card to add.

        Raises:
            TypeError: If the item is not a Card instance.
        """
        if not isinstance(item, Card):
            raise TypeError("Only Card instances can be added to CardCollection")
        return super().append(item)
    
    def shuffle(self):
        """
        Shuffles the cards in the collection.
        """
        random.shuffle(self.data)
        return

class StandardDeck(CardCollection, FrenchSuit):
    """
    Represents a standard deck of playing cards.
    """
    def __init__(self):
        """
        Initializes a standard deck with all 52 playing cards.
        """
        super().__init__()
        self.data = [PlayingCard(suit, rank) for suit in self.SUITS for rank in self.RANKS]

    def deal(self, num_cards: int = 1) -> CardCollection:
        """
        Deals a specified number of cards from the deck.

        Args:
            num_cards (int): The number of cards to deal.

        Returns:
            CardCollection: A collection of dealt cards.

        Raises:
            ValueError: If the number of cards to deal is invalid.
        """
        if num_cards > len(self.data):
            raise ValueError("Not enough cards in the deck to deal")
        elif num_cards <= 0:
            raise ValueError("Number of cards to deal must be positive")
        
        dealt_cards = CardCollection(self.data[:num_cards])
        self.data = self.data[num_cards:]
        return dealt_cards