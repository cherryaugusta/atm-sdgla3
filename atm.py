#!/usr/bin/env python3
"""
Command-Line ATM System

A simple educational simulation of an ATM transaction processor.
"""

# ----------------------------
# INITIAL ACCOUNT STATE
# ----------------------------

# Global variable representing the user's account balance.
# Stored as float to support decimal currency values.
balance = 1000.0


# ----------------------------
# UTILITY FUNCTIONS
# ----------------------------

def display_balance(current_balance):
    """
    Display the current account balance.

    :param current_balance: float representing the account balance
    """
    # Format the balance to two decimal places to simulate currency.
    print(f"Current balance: ${current_balance:.2f}")


def deposit(current_balance, amount):
    """
    Deposit money into the account.

    :param current_balance: float representing the current balance
    :param amount: float representing the deposit amount
    :return: updated balance after deposit
    """
    # Validate that the deposit amount is positive.
    if amount <= 0:
        print("Deposit amount must be greater than zero.")
        return current_balance

    # Add the deposit amount to the balance.
    current_balance += amount

    # Confirm successful transaction to the user.
    print(f"Deposit successful. New balance: ${current_balance:.2f}")

    # Return the updated balance to the caller.
    return current_balance


def withdraw(current_balance, amount):
    """
    Withdraw money from the account.

    :param current_balance: float representing the current balance
    :param amount: float representing the withdrawal amount
    :return: updated balance after withdrawal
    """
    # Validate that the withdrawal amount is positive.
    if amount <= 0:
        print("Withdrawal amount must be greater than zero.")
        return current_balance

    # Prevent overdraft by ensuring sufficient funds exist.
    if amount > current_balance:
        print("Insufficient funds. Transaction declined.")
        return current_balance

    # Deduct the withdrawal amount from the balance.
    current_balance -= amount

    # Confirm successful transaction to the user.
    print(f"Withdrawal successful. New balance: ${current_balance:.2f}")

    # Return the updated balance to the caller.
    return current_balance


# ----------------------------
# MAIN APPLICATION LOOP
# ----------------------------

def run_atm():
    """
    Run the ATM interface loop.
    """
    global balance  # Declare balance as global to allow updates within this function.

    # Infinite loop to keep the ATM running until the user exits.
    while True:
        # Display the ATM menu options.
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        # Prompt the user for their menu choice.
        choice = input("Choose an option (1-4): ").strip()

        # Handle balance inquiry.
        if choice == "1":
            display_balance(balance)

        # Handle deposit transaction.
        elif choice == "2":
            try:
                # Convert user input into a floating-point number.
                amount = float(input("Enter deposit amount: "))
                balance = deposit(balance, amount)
            except ValueError:
                # Catch non-numeric input errors.
                print("Invalid input. Please enter a numeric value.")

        # Handle withdrawal transaction.
        elif choice == "3":
            try:
                # Convert user input into a floating-point number.
                amount = float(input("Enter withdrawal amount: "))
                balance = withdraw(balance, amount)
            except ValueError:
                # Catch non-numeric input errors.
                print("Invalid input. Please enter a numeric value.")

        # Handle exit condition.
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye.")
            break

        # Handle invalid menu selections.
        else:
            print("Invalid choice. Please select a number between 1 and 4.")


# ----------------------------
# PROGRAM ENTRY POINT
# ----------------------------

if __name__ == "__main__":
    # Start the ATM application.
    run_atm()
