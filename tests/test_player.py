import pytest
from gametools.player import Player, CardPlayer

class TestCardPlayer:
    @pytest.fixture
    def player(self):
        return CardPlayer(name="Poker Player")
    
    def test_initialization(self, player: CardPlayer):
        assert player.name == "Poker Player"
        assert len(player.hand) == 0
        assert player.bank.balance == 100.0 # pyright: ignore[reportOptionalMemberAccess]

    def test_give_funds(self, player: CardPlayer):
        recipient = CardPlayer(name="Recipient", starting_balance=50.0)
        player.give(30.0, to=recipient)
        
        assert player.bank.balance == 70.0 # pyright: ignore[reportOptionalMemberAccess]
        assert recipient.bank.balance == 80.0 # pyright: ignore[reportOptionalMemberAccess]

    def test_give_funds_no_bank(self, player: CardPlayer):
        recipient = Player(name="Recipient")
        
        with pytest.raises(ValueError, match="does not have a bank"):
            player.give(30.0, to=recipient)

        with pytest.raises(ValueError, match="does not have a bank"):
            recipient.give(30.0, to=player)