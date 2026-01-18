class CreditCard:

    def __init__(self, customer, bank, accnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = accnt
        self._limit = limit
        self._balance = 0

    @property
    def customer(self):
        return self._customer

    @property
    def bank(self):
        return self._bank

    @property
    def account(self):
        return self._account

    @property
    def limit(self):
        return self._limit

    @property
    def balance(self):
        return self._balance

    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        self._balance -= amount
