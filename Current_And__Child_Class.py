class CurrentAccount(Account):
    def init(self, account_number, account_holder, balance=0):
        super().init(account_number, account_holder, balance)

    def get_account_type(self):
        return "Current"


class ChildrensAccount(Account):
    def init(self, account_number, account_holder, balance=0):
        super().init(account_number, account_holder, balance)
        self._interest_rate = 0.007

    def deposit(self, amount):
        interest = amount * self._interest_rate
        message = super().deposit(amount + interest)
        return message + f" (Interest gained: ₦{interest:.2f})"

    def withdraw(self, amount):
        return "Withdrawals are not allowed from children's accounts."

    def get_account_type(self):
        return "Children's"