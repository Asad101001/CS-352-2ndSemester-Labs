from predatory_credit_card import PredatoryCreditCard

c1 = PredatoryCreditCard("Asad", "MCB", "6969 6969 6969 6969", 2500,0.0825)

c1.charge(100)

c1.process_month()
print(c1.balance)