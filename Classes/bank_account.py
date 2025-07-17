from typing import ClassVar

class Account:
    total_accounts: ClassVar[int] = 0

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self._balance = balance

        Account.total_accounts += 1
        print(f"Account created {self.owner} - Balance: {self._balance:.2f}")
        print(f"Total accounts: {Account.total_accounts}")

    @property
    def balance(self) -> float:
        return self._balance
    
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self._balance += amount
        print(f"{self.owner} deposited ${amount:.2f}. New balance is {self._balance:.2f}.")

    def withdraw(self, amount: float) -> None:
        if amount > self._balance:
            raise ValueError("Insufficient Funds.")
        self._balance -= amount
        print(f"{self.owner} withdrew {amount:.2f}. New balance: {self._balance:.2f}")


def main():
    acct = Account('Alex', 100)
    acct.deposit(50)
    acct.withdraw(25)

if __name__ == "__main__":
    main()