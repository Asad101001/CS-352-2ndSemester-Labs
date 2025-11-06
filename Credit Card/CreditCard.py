class CreditCard:
    def __init__(self,customer,bank,account,balance,limit):
        self._customer = customer
        self._bank = bank
        self._account = account
        self._balance = int(balance)
        self._limit = limit

#Getters of all the attributes of object using 'property' decorator
    @property
    def get_customer( self ):
        return self._customer
    def get_bank( self ):
        return self._bank
    def get_account( self ):
        return self._account
    def get_balance( self ):
        return self._balance
    def get_limit( self ):
        return self._limit

#Transaction from card on assumption amount is within limit
    def charge( self,price ):
        if price + self._balance > self._limit:     #amount is not within limit = transaction not allowed
            return False
        else:
            self._balance += price
            return True
    def make_payment( self , amount):
        self._balance -= amount