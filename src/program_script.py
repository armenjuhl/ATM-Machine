# Entire program accessible to be run as a script
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

def main():
    atm = ATM()
    command = ''
    while command.lower() != 'exit':
        command = input('What would you like to do (deposit, withdraw, check balance, history)\n$ ')

        # Case: Deposit
        if command == 'deposit':
            amount = 0
            deposit = False
            while deposit is False:
                try:
                    amount = input('How much would you like to deposit\n$ ')
                    if amount.lower() == 'exit':
                        break
                    amount = int(amount)
                    atm.deposit(amount)
                    response = input('Thank you for your business. Would you like to do anything else? (y/n)\n')
                    if response.lower == 'yes' or response == 'y':
                        withdraw = True
                    else:
                        print('Have a great day')
                        return True
                    break

                except Exception as TypeError:
                    print('Must enter a valid number. Enter exit to go back.')

        # Case: Withdraw
        if command == 'withdraw':
            amount = 0
            withdraw = False
            while withdraw is False:
                try:
                    amount = input('How much would you like to withdraw\n$ ')
                    if amount == 'exit':
                        break
                    amount = int(amount)
                    withdrawal = atm.withdraw(amount)
                    response = input('Thank you for your business. Would you like to do anything else? (y/n)\n')
                    if response.lower == 'yes' or response == 'y':
                        withdraw = True
                    else:
                        print('Have a great day')
                        return withdrawal

                except Exception as TypeError:
                    print('Must enter a valid number. Enter exit to go back.')

        # Case: Check balance
        if command.lower() == 'check balance' or command.lower() =='balance':
            balance = atm.check_balance()
            print(f"Balance: ${balance}")
            response = input('Thank you for your business. Would you like to do anything else? (y/n)\n')
            if response.lower != 'yes' or response != 'y':
                continue
            else:
                print('Have a great day')
                return True

        # Case: History
        if command.lower() == 'history':
            atm.print_transactions()


if __name__ == '__main__':
    main()
