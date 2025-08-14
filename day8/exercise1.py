
class Account:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def display_balance(self):
        print(f"Balance: ${self.__balance:.2f}")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Account({self.account_number}): {self.account_holder}"

    def __eq__(self, other):
        return self.account_number == other.account_number



class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if self.get_balance() - amount < 100:
            print("Cannot withdraw. Minimum balance of $100 required.")
        else:
            super().withdraw(amount)



class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.get_balance() - amount < -self.overdraft_limit:
            print("Withdrawal exceeds overdraft limit.")
        else:
            self._Account__balance -= amount  



print("🔹 Exercise 1: Banking System")
acc1 = SavingsAccount("123", "Alice", 500, 0.03)
acc2 = CheckingAccount("456", "Bob", 200, 300)

acc1.withdraw(450)
acc2.withdraw(400)

print(acc1)
acc1.display_balance()
print(acc1 == acc2)
print()
