import pytest
from gametools.cards import PlayingCard, StandardDeck

class TestCard:
    def test_valid_card_creation(self):
        with pytest.raises(ValueError):
            PlayingCard('X', 'A')  # Invalid suit
        with pytest.raises(ValueError):
            PlayingCard('❤', '1')  # Invalid rank

        card = PlayingCard(suit='❤', rank='A')
        assert card.suit == '❤'
        assert card.rank == 'A'
        assert str(card) == '[❤A]'

    def test_comparison_operators(self):
        card1 = PlayingCard('♠', '5')
        card2 = PlayingCard('♦', 'K')
        card3 = PlayingCard('♣', '5')

        assert card1 < card2
        assert card2 > card1
        assert card1 == card3  # Same rank, different suits

        with pytest.raises(TypeError):
            card1 == "NotACard"  # pyright: ignore[reportOperatorIssue, reportUnusedExpression]
            
        with pytest.raises(TypeError):
            card1 < 42  # pyright: ignore[reportOperatorIssue, reportUnusedExpression]

    def test_representation(self):
        card = PlayingCard(suit='♦', rank='10')
        assert str(card) == '[♦10]'
        assert repr(card) == "PlayingCard(suit='♦', rank='10')"

class TestStandardDeck:
    @pytest.fixture
    def standard_deck(self):
        return StandardDeck()

    def test_type_checking(self, standard_deck):
        with pytest.raises(TypeError):
            standard_deck.append("NotACard")  # Attempt to add a non-Card instance
    
    def test_deck_initialization(self, standard_deck):
        assert len(standard_deck.data) == 52  # Standard deck should have 52 cards

    def test_deal(self, standard_deck):
        dealt_cards = standard_deck.deal(5)
        assert len(dealt_cards.data) == 5
        assert len(standard_deck.data) == 47  # Deck size should reduce accordingly

        with pytest.raises(ValueError):
            standard_deck.deal(100)  # Attempt to deal more cards than available
        
        with pytest.raises(ValueError):
            standard_deck.deal(-1)   # Attempt to deal negative number of cards

    def test_cards_property(self, standard_deck):
        cards_str = standard_deck.cards
        assert isinstance(cards_str, str)
        assert len(cards_str.split(',')) == 52  # There should be 52 card representations

    def test_append_card_to_deck(self, standard_deck):
        new_card = PlayingCard(suit='♠', rank='A')
        standard_deck.append(new_card)
        assert new_card in standard_deck.data
        assert len(standard_deck.data) == 53  # Deck size should increase by 1

    def test_shuffle_and_sort(self, standard_deck):
        original_order = standard_deck.data.copy()
        standard_deck.shuffle()
        assert standard_deck.data != original_order  # Ensure the deck order has changed after shuffling

        standard_deck.sort()
        assert standard_deck.data == sorted(standard_deck.data, key=lambda card: card.sort_rank)
