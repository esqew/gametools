import pytest
from gametools.player import CardPlayer

class TestCardPlayer:
    @pytest.fixture
    def player(self):
        return CardPlayer(name="Poker Player")
    
    def test_initialization(self, player: CardPlayer):
        assert player.name == "Poker Player"
        assert player.hand is not None