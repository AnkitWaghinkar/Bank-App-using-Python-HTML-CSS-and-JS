# Bank App

This is a simple Bank Web App built using **Python (Flask)** and **HTML/CSS/JS**.  
It allows users to:

- Deposit money  
- Withdraw money  
- Check balance  
- View transaction history (stored in `transaction.txt`)

The project demonstrates how to send data from HTML to Python using Flask.

---

## 🌐 Live Demo (Deployed on Render)

🔗 **Live Website:** https://banking-app-url-here.onrender.com/

###Screenshot 
<img width="1002" height="624" alt="image" src="https://github.com/user-attachments/assets/03c4a017-fbd6-4a0b-982a-c29f81049315" />

---
## Features

### Deposit Money
Adds amount, updates balance, logs to `transaction.txt`.

### Withdraw Money
Validates balance, updates amount, logs transaction.

### Check Balance
Shows current account balance.

### Transaction Log
Displays all logs stored in `transaction.txt`.

---

## 🛠 Technologies Used

- **Python (Flask)**  
- **HTML / CSS / JavaScript**  
- **Render (Hosting platform)**  

---

Run Locally
### Install Dependencies
pip install -r requirements.txt

### Run Flask App
python atm.py

###Open in Browser
Go to: http://127.0.0.1:5000/

---

## 📝 Notes

- All transactions are saved to `transaction.txt`  
- Balance resets every time the server restarts (because it's in-memory)  
- Made for learning Flask form handling and backend logic  

---
