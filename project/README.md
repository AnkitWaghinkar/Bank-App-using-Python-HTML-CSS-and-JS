## Sample Practice Project
This project started as a banking program built entirely in Python. I later added an HTML page to practice integrating Flask. This is that python only code. This program allows users to withdraw money, deposit money, check account balance, view transaction history in `transaction.txt`, and exit operation safely.

---

## Features
### Withdraw funds
Withdraw an amount if the balance is sufficient.
The system checks for:
1. Valid numeric input.
2. Positive amount.
3. Sufficient balance.

### Deposit funds
Add funds to your account. Input is validated and recorded in the log.

### Check account balance
Instantly displays the current account balance.

### View transaction log
Every deposit and withdrawal is written to `transaction.txt`.
<img width="630" height="343" alt="image" src="https://github.com/user-attachments/assets/e8e837df-dca6-499e-a5ed-9077d43f8384" />

### Exit program
Ends the session.

---

## Future Improvements
-[X] Add a GUI or connect your existing HTML/CSS/JS frontend to this backend.
-[ ] Add a PIN-based login system.
-[ ] Show timestamps in the transaction log.
-[ ] Prevent negative deposits/withdrawals inside class logic.
-[ ] Create multiple accounts.
-[ ] Store history in a database.

