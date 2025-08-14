class BankAccount:

    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            print(f"✅ Deposited ${amount:.2f} into {self.account_holder}'s account.")
        else:
            print("❌ Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("❌ Insufficient funds.")
        elif amount <= 0:
            print("❌ Withdrawal amount must be positive.")
        else:
            self.__balance -= amount
            print(f"✅ Withdrew ${amount:.2f} from {self.account_holder}'s account.")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"BankAccount(Account Holder: {self.account_holder}, Balance: ${self.__balance:.2f})"


# Example usage
if __name__ == "__main__":
    account1 = BankAccount("Alice", 1000)
    print(account1)

    account1.deposit(500)
    account1.withdraw(200)
    print(f"💰 Current balance: ${account1.get_balance():.2f}")

    account1.withdraw(2000)  # Should trigger insufficient funds
    print(account1)
