# Command-Line ATM System

## Overview

This repository contains a Python-based command-line ATM simulation designed for educational purposes and portfolio demonstration. The project models core ATM behaviors such as balance inquiries, deposits, withdrawals, input validation, and overdraft prevention using clean, modular, and extensible code.

The system emphasizes correctness, readability, and real-world transaction logic while remaining intentionally simple.

---

## Features

- Persistent account state management
- Modular function-based design
- Input validation for all transactions
- Overdraft prevention
- Clear and user-friendly command-line interface
- Easily extensible architecture

---

## Project Structure

.
├── atm.py
└── README.md

---

## Requirements

- Python 3.8 or higher

No external dependencies are required.

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/command-line-atm.git
cd command-line-atm
```
2.	Run the program:
python atm.py

---

## Example Interaction
--- ATM MENU ---
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Choose an option (1-4): 1
Current balance: $1000.00

Choose an option (1-4): 3
Enter withdrawal amount: 1200
Insufficient funds. Transaction declined.

Choose an option (1-4): 2
Enter deposit amount: 500
Deposit successful. New balance: $1500.00

Choose an option (1-4): 4
Thank you for using the ATM. Goodbye.

---

## Core Concepts Demonstrated
•	State management
•	Input validation and error handling
•	Business rule enforcement
•	Modular function design
•	Continuous program execution with controlled exit conditions

---

## Real-World Relevance
This project reflects simplified versions of logic found in:
•	ATM terminals
•	Mobile banking applications
•	Teller systems
•	Payment kiosks
The same principles demonstrated here scale to enterprise-grade financial systems.

---

## Extensibility Ideas
•	PIN authentication
•	Multiple user accounts
•	Transaction history logging
•	Daily withdrawal limits
•	Persistent storage (files or databases)

---

## Disclaimer
This project is provided strictly for educational and portfolio demonstration purposes.
It does not implement real banking security, encryption, authentication, auditing, or regulatory compliance mechanisms.
It must not be used in production environments or for handling real financial data.
