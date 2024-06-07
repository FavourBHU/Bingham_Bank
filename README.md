# Bingham Bank Application

## Overview
Bingham Bank is a Python-based GUI application for managing different types of bank accounts. The application uses the Tkinter library for the graphical user interface and supports various account types including Savings, Current, Children's, and Student accounts. Each account type has specific rules for deposits and withdrawals, and the application calculates interest for eligible accounts. The app features encapsulation, inheritance, and polymorphism to manage account operations efficiently.

## Features
- **Account Creation**: Users can create different types of accounts (Savings, Current, Children's, and Student).
- **Deposits and Withdrawals**: Allows users to deposit and withdraw money according to the rules of each account type.
- **Interest Calculation**: Automatically calculates interest on deposits for Savings and Children's accounts.
- **Balance Inquiry**: Users can check the balance of their accounts.
- **Account Management**: Displays a dropdown of created account numbers for easy management.
- **User Interface**: A clean, black and white themed GUI for easy interaction.

## Account Types and Rules
1. **Savings Account**
   - Interest Rate: 0.5% per deposit.
   - Withdrawal Limit: ₦700,000 per transaction.

2. **Current Account**
   - No restrictions on deposits or withdrawals.

3. **Children's Account**
   - Interest Rate: 0.7% per deposit.
   - Withdrawals are not allowed.

4. **Student Account**
   - Withdrawal Limit: ₦2,000 per transaction.
   - Deposit Limit: ₦50,000 per deposit.

## Usage
### Creating an Account
1. **Enter Name**: Type your name in the 'Name' field.
2. **Enter Initial Balance**: Type the initial balance amount in the 'Initial Balance' field.
3. **Select Account Type**: Choose the desired account type from the dropdown menu.
4. **Create Account**: Click the "Create Account" button. A new account number will be generated and displayed.

### Making a Deposit
1. **Select Account Number**: Choose the account number from the dropdown menu.
2. **Enter Deposit Amount**: Type the deposit amount in the 'Deposit Amount' field.
3. **Deposit**: Click the "Deposit" button. The amount, including any interest, will be deposited into the selected account.

### Making a Withdrawal
1. **Select Account Number**: Choose the account number from the dropdown menu.
2. **Enter Withdraw Amount**: Type the withdrawal amount in the 'Withdraw Amount' field.
3. **Withdraw**: Click the "Withdraw" button. The amount will be withdrawn from the selected account, subject to account-specific rules.

### Checking Balance
1. **Select Account Number**: Choose the account number from the dropdown menu.
2. **Check Balance**: Click the "Get Balance" button. The current balance will be displayed in a message box.

## Code Structure
- **Account Classes**: The `Account` class and its subclasses (`SavingsAccount`, `CurrentAccount`, `ChildrensAccount`, `StudentAccount`) encapsulate the properties and behaviors of each account type.
- **BankApp Class**: The `BankApp` class handles the GUI and user interactions.
- **Main Application**: The `__main__` section initializes the Tkinter root and runs the application.


# Contributor
**Favour Lawrence Ejiogu - BHU/23/04/09/0058 - GROUP LEADER**
