class ATM:
    """A class of an ATM machine"""
    def __init__(self):
        self.balance = 0
        self.interest_rate = 0.1
        self.transactions = list()

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        try:
            self.balance += amount
            self.transactions.append(f"user deposited ${amount}")
            print(f"${amount} deposited into account")
        except TypeError:
            print('Invalid type')
        # return True

    def check_withdrawal(self, amount):
        if self.balance - amount >= 0:
            return True
        else:
            return False

    def withdraw(self, amount):
        if self.check_withdrawal(amount) is True:
            self.balance -= amount
            self.transactions.append(f"user withdrew ${amount}")
            print('Withdrawal successful')
            return amount
        else:
            print('Insufficient funds')

    def calc_interest(self):
        return self.interest_rate

    def print_transactions(self):
        print(f"Transactions: {self.transactions}")
