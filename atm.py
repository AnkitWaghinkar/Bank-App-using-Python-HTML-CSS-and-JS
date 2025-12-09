from flask import Flask, request, render_template

app = Flask(__name__)

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
            return "Invalid amount"

        if amount <= 0:
            return "Withdrawal must be positive"

        if amount > self.balance:
            return "Insufficient funds"

        self.balance -= amount
        self.transaction_log(f"Withdrew {amount}")
        return f"Withdrawn {amount}. New balance = {self.balance}"

    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            return "Invalid amount"

        if amount <= 0:
            return "Deposit must be positive"

        self.balance += amount
        self.transaction_log(f"Deposited {amount}")
        return f"Deposited {amount}. New balance = {self.balance}"


account = bank(1000)


# Serve HTML page
@app.route('/')
def home():
    return render_template('index.html')


# Withdraw route
@app.route('/withdraw', methods=['POST'])
def withdraw():
    amount = request.form['amount']
    result = account.withdraw(amount)
    return result


# Deposit route
@app.route('/deposit', methods=['POST'])
def deposit():
    amount = request.form['amount']
    result = account.deposit(amount)
    return result


# Check balance route
@app.route('/balance')
def balance():
    return f"Current Balance: {account.balance}"


#Transactions log
@app.route('/transaction')
def transactions():
    try:
        with open("transaction.txt", "r") as file:
            content = file.read().replace("\n", "<br>")
    except FileNotFoundError:
        content = "No transactions found."
    
    return f"<h2>Transaction History</h2><p>{content}</p>"


if __name__ == "__main__":
    app.run(debug=True)
