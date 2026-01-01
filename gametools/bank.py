class Bank:
    """Base class representing a bank with a balance."""
    balance: float

    def withdraw(self, amount: float | int) -> float:
        """
        Withdraw an amount from the bank.

        Args:
            amount (float | int): The amount to withdraw.

        Returns:
            float: The withdrawn amount.

        Raises:
            ValueError: If the amount is non-positive or exceeds the current balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds in bank")
        
        self.balance -= amount
        return amount
    
    def deposit(self, amount: float | int) -> None:
        """
        Deposit an amount into the player's bank.

        Args:
            amount (float | int): The amount to deposit.

        Raises:
            ValueError: If the amount is non-positive.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self.balance += amount
        return
    
    def give(self, amount: float | int, to: 'Bank') -> None:
        """
        Transfer an amount from this `Bank` to another `Bank`.

        Args:
            amount (float | int): The amount to transfer.
            recipient (Bank): The target `Bank` to receive the funds.
        Raises:
            ValueError: If the amount is non-positive or exceeds the current balance.
        """
        return to.deposit(self.withdraw(amount=amount))

class PlayerBank(Bank):
    """Represents a player's bank with a finite balance."""

    def __init__(self, starting_balance: float = 100.0):
        """
        Initialize the player's bank with a starting balance.

        Args:
            starting_balance (float): The initial balance for the player. Defaults to 100.0.
        """
        self.balance = starting_balance

class HouseBank(Bank):
    """Represents the house bank with an infinite balance."""

    def __init__(self):
        """
        Initialize the house bank with an infinite balance.
        """
        super().__init__()
        self.balance = float('inf')
    pass