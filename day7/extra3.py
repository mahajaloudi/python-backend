class BankAccount:
    """
    A simple bank account class with deposit, withdrawal, and balance checking.
    """

    def __init__(self, account_holder, balance=0):
        """
        Initialize the account holder's name and starting balance.
        """
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """
        Deposit a positive amount into the account.
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f} successfully.")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        """
        Withdraw a positive amount if funds are sufficient.
        """
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif amount > self.balance:
            print("Insufficient funds. Withdrawal denied.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} successfully.")

    def get_balance(self):
        """
        Return the current balance.
        """
        return self.balance


# Example usage
account = BankAccount("Alice", 100)
account.deposit(50)
account.withdraw(30)
account.withdraw(200)
print(f"Current balance: ${account.get_balance():.2f}")
