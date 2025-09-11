
import json
from datetime import datetime
import os


class Transaction:
    def __init__(self, amount, category, date=None):
        self.amount = amount
        self.category = category
        self.date = date if date else datetime.today().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "type": self.__class__.__name__
        }


class Income(Transaction):
    pass


class Expense(Transaction):
    pass



class Ledger:
    def __init__(self, filename="transactions.json"):
        self.filename = filename
        self.transactions = []
        self.load_data()

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self.save_data()

    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump([t.to_dict() for t in self.transactions], f, indent=4)

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                for t in data:
                    if t["type"] == "Income":
                        self.transactions.append(Income(t["amount"], t["category"], t["date"]))
                    elif t["type"] == "Expense":
                        self.transactions.append(Expense(t["amount"], t["category"], t["date"]))

    def view_transactions(self):
        if not self.transactions:
            print("\nNo transactions recorded yet.\n")
            return
        print("\n==== Transaction History ====")
        for idx, t in enumerate(self.transactions, 1):
            print(f"{idx}. {t.date} | {t.category} | {t.__class__.__name__} | {t.amount}")
        print("=============================\n")

    def summary(self):
        income = sum(t.amount for t in self.transactions if isinstance(t, Income))
        expenses = sum(t.amount for t in self.transactions if isinstance(t, Expense))
        balance = income - expenses

        print("\n==== Financial Summary ====")
        print(f"Total Income : {income}")
        print(f"Total Expense: {expenses}")
        print(f"Net Balance  : {balance}")
        print("===========================\n")



def main():
    ledger = Ledger()

    while True:
        print("==== Personal Finance Tracker ====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. View Summary")
        print("5. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                amount = float(input("Enter income amount: "))
                category = input("Enter category (e.g., Salary): ")
                ledger.add_transaction(Income(amount, category))
                print("✅ Income added!\n")

            elif choice == "2":
                amount = float(input("Enter expense amount: "))
                category = input("Enter category (e.g., Groceries): ")
                ledger.add_transaction(Expense(amount, category))
                print("✅ Expense added!\n")

            elif choice == "3":
                ledger.view_transactions()

            elif choice == "4":
                ledger.summary()

            elif choice == "5":
                print("👋 Exiting... Have a nice day!")
                break

            else:
                print("❌ Invalid choice, please try again.\n")

        except ValueError:
            print("❌ Invalid input. Please enter a valid number.\n")


if __name__ == "__main__":
    main()
