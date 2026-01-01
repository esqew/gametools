import pytest
from gametools.bank import PlayerBank, HouseBank

class TestPlayerBank:
    @pytest.fixture
    def bank(self):
        b = PlayerBank(starting_balance=200.00)
        return b
    
    def test_deposit(self, bank):
        bank.deposit(50)
        assert bank.balance == 250.00

    def test_invalid_deposit(self, bank):
        with pytest.raises(ValueError, match="Deposit amount must be positive"):
            bank.deposit(-20)

    def test_withdrawal_success(self, bank):
        amount = bank.withdraw(100)
        assert amount == 100
        assert bank.balance == 100.00

    def test_withdraw_insufficient_funds(self, bank):
        with pytest.raises(ValueError, match="Insufficient funds in bank"):
            bank.withdraw(300)

    def test_invalid_withdrawral(self, bank):
        with pytest.raises(ValueError, match="Withdrawal amount must be positive"):
            bank.withdraw(-100)

    def test_give_funds(self, bank):
        recipient_bank = PlayerBank(starting_balance=50.00)
        bank.give(75, to=recipient_bank)
        assert bank.balance == 125.00
        assert recipient_bank.balance == 125.00

class TestHouseBank:
    @pytest.fixture
    def bank(self):
        b = HouseBank()
        return b
    
    def test_withdrawral_always_succeeds(self, bank):
        bank.withdraw(1000000)
        assert bank.balance == float('inf')