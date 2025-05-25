# Enhanced Bank Account Management System

# 🏦 Data Structures to Store Information
# Store data using nested dictionaries. Key -> account number. Values: Account holder and PIN.
accounts = {}

transaction_histories = {}  # Account transaction logs
loans = {}       # Account loan details

last_account_number = 10000
MAX_LOAN_AMOUNT = 10000
INTEREST_RATE = 0.0268

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

def account_number_generator(last_acc_num):
    """Generate an account number"""
    last_acc_num += 1

    return last_acc_num

def try_again():
    """This is a function that asks you if you wish to go to the main menu or your wish to exit."""
    pass

def create_name():
    while True:
        first_name = input("Please, enter client's first name: ")
        if not first_name.isalpha():
            print("Invalid first name! Please, try again!")
            continue
        else:
            print("Success! First name saved!")

        surname = input("Please, enter client's surname name: ")
        if not surname.isalpha():
            print("Invalid first name! Please, try again!")
            continue

        name = first_name + " " + surname
        return name


def create_pin_code():
    """Create a PIN code."""
    print('Create a PIN code!')
    while True:
        pin = input('Enter four digits: ')
        if len(pin) != 4 or not pin.isdigit():
            print('Invalid PIN. Try again!')
            continue
        else:
            print("Success!")
        return int(pin)

def save_to_a_file():
    """This function gives you the opportunity to save the result you asked for in a file."""
    pass

def create_account():
    """Create a new account."""
    account_number = account_number_generator(last_account_number)
    name = create_name()
    balance = 0.00

    accounts[account_number] = {"Name": name, "Balance": balance}


def deposit():
    """Deposit money into an account."""
    while True:
        print('Follow the steps to make a deposit!')
        acc_num = int(input('Please, enter your account number: '))

        if acc_num in accounts.keys():
            print('We\'ve found the account.')
            name = input('Please, enter fullname: ')
            if name == accounts[acc_num]["Name"]:
                print("Success!")
                print()
                print("You can make a deposit")
                print()
                current_deposit = float(input('Enter amount: '))
                print("Enter Admin PIN to confirm the transaction: ")
                check_admin_pin = int(input())
                if check_admin_pin == admin_pin_code:
                    print("Success! Transaction confirmed!")
                    accounts[acc_num]["Balance"] += current_deposit
                    transaction_histories[acc_num] = {"Deposit": current_deposit}
                    break
                else:
                    print("Sorry! Wrong PIN! You need to start over")
                    break
            else:
                print("Wrong Name. This Name does not match the name on the account.\n")
                print('Would you like to try again? - 1-> Yes 2-> No: ')
                answer = input()
                if answer == '1':
                    continue
                else:
                    break
        else:
            print("We couldn't find the account\n")
            print('Would you like to try again? - 1-> Yes 2-> No: ')
            answer = input()
            if answer == '1':
                continue
            else:
                break


def withdraw():
    """Withdraw money from an account."""
    while True:
        print('Follow the steps to withdraw money!')
        acc_num = int(input('Please, enter the account number: '))

        if acc_num in accounts.keys():
            print('We\'ve found the account.')
            name = input('Please, enter fullname: ')
            if name == accounts[acc_num]["Name"]:
                print("Success!")
                print()
                print("You can withdraw money!")
                print()

                current_withdraw = float(input('Enter amount: '))
                print("Enter Admin PIN to confirm the transaction: ")
                check_admin_pin = int(input())
                if check_admin_pin == admin_pin_code:
                    print("Success! Transaction confirmed!")
                    accounts[acc_num]["Balance"] -= current_withdraw
                    transaction_histories[acc_num] = {"Withdraw": current_withdraw}
                    break
                else:
                    print("Sorry! Wrong PIN! You need to start over")
                    break
            else:
                print("Wrong Name. This Name does not match the name on the account.\n")
                print('Would you like to try again? - 1-> Yes 2-> No: ')
                answer = input()
                if answer == '1':
                    continue
                else:
                    break
        else:
            print("We couldn't find the account\n")
            print('Would you like to try again? - 1-> Yes 2-> No: ')
            answer = input()
            if answer == '1':
                continue
            else:
                break

def check_balance():
    """Check balance of an account."""
    while True:
        print('Follow the steps to check a balance!')
        acc_num = int(input('Please, enter account number: '))

        if acc_num in accounts.keys():
            print('We\'ve found the account.')
            name = input('Please, enter fullname: ')
            if name == accounts[acc_num]["Name"]:
                print("Success!")
                print()
                print("Enter Admin PIN to confirm the transaction: ")
                check_admin_pin = int(input())
                if check_admin_pin == admin_pin_code:
                    print("Success!")
                    print()
                    print(f"Account number: {acc_num} | "
                          f"Name: {accounts[acc_num]['Name']} | "
                          f"Balance: {accounts[acc_num]['Balance']} EUR")
                    break
                else:
                    print("Sorry! Wrong PIN! You need to start over")
                    break
            else:
                print("Wrong Name. This Name does not match the name on the account.\n")
                print('Would you like to try again? - 1-> Yes 2-> No: ')
                answer = input()
                if answer == '1':
                    continue
                else:
                    break
        else:
            print("We couldn't find your account\n")
            print('Would you like to try again? - 1-> Yes 2-> No: ')
            answer = input()
            if answer == '1':
                continue
            else:
                break

def list_accounts():
    """List all account holders and details."""
    print("To get a list of all of the accounts, enter Admin PIN: ")
    check_admin_pin = int(input())
    for account, values in accounts.items():
        if check_admin_pin == admin_pin_code:
            print()
            print(f"Account number: {account} | "
                  f"Name: {values['Name']} | "
                  f"Balance: {values['Balance']} EUR")
        else:
            print("Sorry! Wrong PIN! You need to start over")
            break
    print("Success!")
def transfer_funds():
    """Transfer funds between two accounts."""

    # 1. Ask for the account number of the sender!
    # 2. Check if the account exists!
    # 3. Find the name of the account in the system!
    # 4. Ask if the name of the account is correct!
    # 5. Ask for the account number of the receiver!
    # 6. Check if the account exists!
    # 7. Find the name of the account in the system!
    # 8. Ask if the name of the account is correct!
    # 9. Ask what amount to transfer!
    # 10. Ask for confirmation and PIN of the user!
    # 11. Minus the account of the sender and plus the account of the receiver!
    # 12. Save the transaction in the transaction log!
    # 13. Inform that the transaction went through successfully!
    while True:
        print('Follow the steps to maka a transfer!')
        acc_num = int(input('Please, enter an account number of the sender: '))

        if acc_num in accounts.keys():
            print('We\'ve found the account.')
            name = input('Please, enter fullname: ')
            if name == accounts[acc_num]["Name"]:
                print("Success!")
                print()
                print("You can make the transfer")
                print()
                receiver_account_number = int(input('Please, enter the number of the receiving account: '))
                current_transfer = float(input('Enter amount: '))
                if receiver_account_number in accounts.keys():
                    print("Enter Admin PIN to confirm the transaction: ")
                    check_admin_pin = int(input())
                    if check_admin_pin == admin_pin_code:
                        print("Success! Transaction confirmed!")
                        accounts[acc_num]["Balance"] -= current_transfer
                        accounts[receiver_account_number]["Balance"] += current_transfer
                        transaction_histories[acc_num] = {"Sent": current_transfer}
                        transaction_histories[receiver_account_number] = {"Received": current_transfer}
                        break
                    else:
                        print("Sorry! Wrong PIN! You need to start over")
                        break
                else:
                    print("Enter Admin PIN to confirm the transaction: ")
                    check_admin_pin = int(input())
                    if check_admin_pin == admin_pin_code:
                        print("Success! Transaction confirmed!")
                        accounts[acc_num]["Balance"] -= current_transfer
                        transaction_histories[acc_num] = {"Sent": current_transfer}
                        break
                    else:
                        print("Sorry! Wrong PIN! You need to start over")
                        break
            else:
                print("Wrong Name. This Name does not match the name on the account.\n")
                print('Would you like to try again? - 1-> Yes 2-> No: ')
                answer = input()
                if answer == '1':
                    continue
                else:
                    break
        else:
            print("We couldn't find the account\n")
            print('Would you like to try again? - 1-> Yes 2-> No: ')
            answer = input()
            if answer == '1':
                continue
            else:
                break

def view_transaction_history():
    """View transactions for an account."""
    pass  # TODO: Add logic
    # 1. Ask if the needed info is for a specific account or in general!
    # 2. Check if the account exists!
    # 3. For a specific account ask for the account number!#
    # 4. Find the name of the account in the system!
    # 5. Ask if the name of the account is correct!
    # 6. Ask for confirmation and PIN of the user! Pin verifier function needed!
    # 7. Show the transactions and offer to save it in a file!
    # 8. Do you wish to continue function!


def apply_for_loan():
    """Allow user to apply for a loan."""
    pass  # TODO: Add logic

def repay_loan():
    """Allow user to repay a loan."""
    pass  # TODO: Add logic

def identify_card_type():
    """Identify type of credit card."""
    pass  # TODO: Add logic



print("Hello, Admin! \nBefore you get access to this program you need to create a PIN code!")
admin_pin_code = create_pin_code()
print(admin_pin_code)
while True:
    display_menu()
    choice = int(input("Enter your choice: "))
    # Map choices to functions
    if choice == 1:
        create_account()
        last_account_number += 1
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        check_balance()
    elif choice == 5:
        list_accounts()
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


