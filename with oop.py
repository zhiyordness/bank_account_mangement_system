

accounts = {}

for _ in range(3):
    acc_number = int(input())
    balance = float(input())
    name = input()
    accounts[acc_number] = {"Name": name, "Balance": balance}


print(accounts)