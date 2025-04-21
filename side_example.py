# Enhanced Bank Account Management System

# 🏦 Data Structures to Store Information
account_holders = []  # Account names
pin_codes = []
account_numbers = []
balances = []  # Account balances
transaction_histories = []  # Account transaction logs
loans = []  # Account loan details

account_number = 1000
MAX_LOAN_AMOUNT = 10000
INTEREST_RATE = 0.03


def display_menu():
    """Main menu for banking system."""
    print("\n🌟 Welcome to Enhanced Bank System 🌟")
    print("1️⃣ Create Account")
    print("2️⃣ Deposit Money")
    print("3️⃣ Withdraw Money")
    print("4️⃣ Check Balance")
    print("5️⃣ List All Accounts")
    print("6️⃣ Transfer Funds")
    print("7️⃣ View Transaction History")
    print("8️⃣ Apply for Loan")
    print("9️⃣ Repay Loan")
    print("🔟 Identify Credit Card Type")
    print("0️⃣ Exit")


def create_account(name: str, pin: str, number_of_account: int, money: int):
    """Create a new account."""
    account_holders.append(name)
    pin_codes.append(pin)
    account_numbers.append(number_of_account)
    balances.append(money)

    print('You successfully registered your account!')

def deposit():
    """Deposit money into an account."""
    while True:
        print('Follow the steps to make a deposit!')
        full_name = input('Please, enter your full name: ')

        if full_name in account_holders:
            index = account_holders.index(full_name)
            print('We\'ve found your account.')
            pin_code = input('Please, enter your PIN: ')
            if pin_code in pin_codes:
                if pin_code == pin_codes[index]:
                    print("Make a deposit")
                    print()
                    print("NOTE: If the amount you wish to deposit is more than 10000 BGN you must fill out"
                          " a declaration form about the money origin. "
                          "In such case we are obliged by law to contact you and investigate!")
                    deposit = float(input('Enter amount: '))
                    balances[index] += deposit

                    print('Success!')
                    break
            else:
                print("Wrong PIN. This PIN does not exist.\n")
                print('Would you like to try again? - 1-> Yes 2-> No: ')
                answer = input()
                if answer == '1':
                    # pin_code = input('Please, enter your PIN: ')
                    continue
                else:
                    break

        else:
            print("We couldn't find your account\n")
            print('Would you like to try again? - 1-> Yes 2-> No: ')
            answer = input()
            if answer == '1':
                # full_name = input('Please, enter your full name: ')
                continue
            else:
                break



def withdraw():
    """Withdraw money from an account."""
    while True:
        print('Follow the steps to withdraw money!')
        full_name = input('Please, enter your full name: ')

        if full_name in account_holders:
            index = account_holders.index(full_name)
            print('We\'ve found your account.')
            pin_code = input('Please, enter your PIN: ')
            if pin_code in pin_codes:
                if pin_code == pin_codes[index]:
                    print("Make a withdrawal")
                    print()
                    withdraw_amount = float(input('Enter amount: '))
                    if withdraw_amount <= balances[index]:
                        balances[index] -= withdraw_amount
                        print('Success!')
                        break
                    else:
                        print(f'Not enough money! Try another amount! Your current balance is {balances[index]} BGN.')
                        continue

            else:
                print("Wrong PIN. This PIN does not exist.\n")
                print('Would you like to try again? - 1-> Yes 2-> No: ')
                answer = input()
                if answer == '1':
                    # pin_code = input('Please, enter your PIN: ')
                    continue
                else:
                    break

        else:
            print("We couldn't find your account\n")
            print('Would you like to try again? - 1-> Yes 2-> No: ')
            answer = input()
            if answer == '1':
                # full_name = input('Please, enter your full name: ')
                continue
            else:
                break

def check_balance():
    """Check balance of an account."""
    while True:
        print('Follow the steps to check your balance!')
        full_name = input('Please, enter your full name: ')

        if full_name in account_holders:
            index = account_holders.index(full_name)
            print('We\'ve found your account.')
            pin_code = input('Please, enter your PIN: ')
            if pin_code in pin_codes:
                if pin_code == pin_codes[index]:
                    print(f"Your balance if {balances[index]} BGN.")
                    break
            else:
                print("Wrong PIN. This PIN does not exist.\n")
                print('Would you like to try again? - 1-> Yes 2-> No: ')
                answer = input()
                if answer == '1':
                    # pin_code = input('Please, enter your PIN: ')
                    continue
                else:
                    break

        else:
            print("We couldn't find your account\n")
            print('Would you like to try again? - 1-> Yes 2-> No: ')
            answer = input()
            if answer == '1':
                # full_name = input('Please, enter your full name: ')
                continue
            else:
                break


def list_accounts(num_acts: list, accounts: list, money_list: list ):
    """List all account holders and details."""
    result = ''
    for index in range(0, len(num_acts)):
        result += (f'Account number: {num_acts[index]} | '
                   f'Names: {accounts[index]} | '
                   f'Balance: {float(money_list[index])} BGN\n')
    return result


def transfer_funds():
    """Transfer funds between two accounts."""
    pass  # TODO: Add logic


def view_transaction_history():
    """View transactions for an account."""
    pass  # TODO: Add logic


def apply_for_loan():
    """Allow user to apply for a loan."""
    pass  # TODO: Add logic


def repay_loan():
    """Allow user to repay a loan."""
    pass  # TODO: Add logic


def identify_card_type():
    """Identify type of credit card."""
    pass  # TODO: Add logic


def create_pin_code():
    """Create a PIN code."""
    print('Create a PIN code!')
    while True:
        pin = input('Enter four digits: ')
        if len(pin) != 4:
            print('Invalid PIN. Try again!')
            continue
        else:
            return pin


while True:
    display_menu()
    choice = int(input("Enter your choice: "))

    # Map choices to functions
    if choice == 1:
        full_name = input('Please, enter your full name: ')
        pin_code = create_pin_code()
        account_number += 1
        current_account_number = account_number
        balance = 0
        create_account(full_name, pin_code, current_account_number, balance)

    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        check_balance()
    elif choice == 5:
        print(list_accounts(account_numbers, account_holders, balances))
    elif choice == 6:
        transfer_funds()
    elif choice == 7:
        view_transaction_history()
    elif choice == 8:
        apply_for_loan()
    elif choice == 9:
        repay_loan()
    elif choice == 10:
        identify_card_type()
    elif choice == 0:
        print("Goodbye! 👋")
        break
    else:
        print("❌ Invalid choice. Try again!")

    print()
    print('Go to the main menu - 1-> Yes 2-> No: ')
    answer = input()
    if answer == '1':
        continue
    else:
        break
