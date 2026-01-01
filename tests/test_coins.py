import pytest
from gametools.coins import Coin, CoinResult

class TestCoins:
    @pytest.fixture
    def coin(self) -> Coin:
        return Coin()
    
    def test_coin_flip(self, coin: Coin) -> None:
        coin.flip()
        assert coin.value in (CoinResult.HEADS, CoinResult.TAILS)

    def test_coin_repr(self, coin: Coin) -> None:
        repr_str = repr(coin)
        assert repr_str.startswith("Coin(value=")
        assert repr_str.endswith(")")