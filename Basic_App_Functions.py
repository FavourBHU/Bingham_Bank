def generate_account_number(self):
    return str(random.randint(1000000000, 9999999999))


def update_account_menu(self):
    menu = self.account_number_menu["menu"]
    menu.delete(0, "end")
    for account_number in self.accounts:
        menu.add_command(label=account_number,
                         command=lambda value=account_number: self.account_number_var.set(value))


def create_account(self):
    name = self.name_entry.get()
    balance = float(self.balance_entry.get())
    account_type = self.account_type_var.get()
    account_number = self.generate_account_number()

    if account_number in self.accounts:
        messagebox.showerror("Error", "Account already exists.")
        return<

    if account_type == "Savings":
        self.accounts[account_number] = SavingsAccount(account_number, name, balance)
    elif account_type == "Current":
        self.accounts[account_number] = CurrentAccount(account_number, name, balance)
    elif account_type == "Children's":
        self.accounts[account_number] = ChildrensAccount(account_number, name, balance)
    elif account_type == "Student":
        self.accounts[account_number] = StudentAccount(account_number, name, balance)

    self.update_account_menu()
    messagebox.showinfo("Success",
                        f"{account_type} account created successfully.\nAccount Number: {account_number}")


def deposit(self):
    account_number = self.account_number_var.get()
    amount = float(self.deposit_amount_entry.get())

    if account_number not in self.accounts:
        messagebox.showerror("Error", "Account does not exist.")
        return

    account = self.accounts[account_number]
    message = account.deposit(amount)
    messagebox.showinfo("Deposit", message)


def withdraw(self):
    account_number = self.account_number_var.get()
    amount = float(self.withdraw_amount_entry.get())

    if account_number not in self.accounts:
        messagebox.showerror("Error", "Account does not exist.")
        return

    account = self.accounts[account_number]
    message = account.withdraw(amount)
    messagebox.showinfo("Withdraw", message)


def get_balance(self):
    account_number = self.account_number_var.get()

    if account_number not in self.accounts:
        messagebox.showerror("Error", "Account does not exist.")
        return

    account = self.accounts[account_number]
    balance = account.get_balance()
    messagebox.showinfo("Balance", f"Balance for account {account_number} is ₦{balance}.")


if name == "main":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop(