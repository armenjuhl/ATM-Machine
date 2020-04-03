from src.AtmClass import ATM


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
