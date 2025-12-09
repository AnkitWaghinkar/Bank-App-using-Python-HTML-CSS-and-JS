class bank:

    def __init__(self, initial_amount = 0.00):
        self.balance = initial_amount

    def transaction_log(self, transaction_string):
        with open("transaction.txt", "a") as file:
            file.write(f"{transaction_string:<20} Balance: {self.balance} \n")

    def withdraw(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount > self.balance:
            print("Insufficient funds!")
            return
        
        self.balance = self.balance - amount
        self.transaction_log(f" Withdrew {amount}")

    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0

        self.balance = self.balance + amount
        self.transaction_log(f" Deposited {amount}")

account = bank(1000)
while True:
    try:
        action = input ("What action would you like to perform: \n" 
                        "-Withdraw \n"
                        "-Deposit \n" 
                        "-Balance \n"
                        "-Exit\n")
    except KeyboardInterrupt:
        print("Leaving the Atm")
        break

    action = action.lower()
    if action == "withdraw":
        amount = input("How much money you want to withdraw? \n")
        account.withdraw(amount)
        
        if float(amount) > account.balance:
            print("Insufficient funds!")
            continue
        
        elif float(amount) <= 0:
            print("Withdrawal amount must be positive!")
            continue

        print(f"Amount withdrawn: {amount}. \n Your Account Balance is {account.balance}")
        continue

    elif action == "deposit":
        amount = input("How much money you want to deposit? \n")
        account.deposit(amount)
        
        if float(amount) <= 0:
            print("Deposit amount must be positive!")
            continue

        print(f"Amount Deposited: {amount}. \n Your Account Balance is {account.balance}")
        continue

    elif action == "balance":
        check = account.balance
        print(f"Account Balance is {check}")
        continue

    elif action == "exit":
        print("Exiting...")
        break

    else: 
        print("Not a valid option try again \n")