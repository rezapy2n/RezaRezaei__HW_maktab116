class BankAccount:
    def __init__(self, account_holder_name, initial_balance, minimum_balance):
        self.account_holder_name = account_holder_name
        self.balance = initial_balance
        self.minimum_balance = minimum_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} units. New balance: {self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance - amount >= self.minimum_balance:
                self.balance -= amount
                print(f"Withdrew {amount} units. New balance: {self.balance}")
            else:
                print("Insufficient funds for withdrawal.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

    def transfer(self, other_account, amount):
        if amount > 0:
            if self.balance - amount >= self.minimum_balance:
                self.balance -= amount
                other_account.deposit(amount)
                print(f"Transferred {amount} units to {other_account.account_holder_name}.")
            else:
                print("Insufficient funds for transfer.")
        else:
            print("Invalid transfer amount. Please enter a positive value.")

# مثال استفاده:
account1 = BankAccount("reza", 1000, 500)
account2 = BankAccount("ali", 2000, 500)

account1.deposit(300)
account1.withdraw(200)
account1.transfer(account2, 400)
