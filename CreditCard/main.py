from credit_card import CreditCard

if __name__ == "__main__":
    wallet = []
    wallet.append(CreditCard("Asad", "MCB", "6969 6969 6969 6969", 2500))
    wallet.append(CreditCard("Asim", "Meezan", "6767 6767 6767 6767", 3500))
    wallet.append(CreditCard("Aslam", "UBL", "4200 4200 4200 4200", 5000))

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2 * val)
        wallet[2].charge(3 * val)

    for c in range(3):
        print("Customer = ", wallet[c].customer)
        print("\tBank = ", wallet[c].bank)
        print("\t\tAccount = ", wallet[c].account)
        print("\t\t\tLimit = ", wallet[c].limit)
        print("\t\t\t\tBalance = ", wallet[c].balance)

        while wallet[c].balance > 100:
            wallet[c].make_payment(100)
            print("New balance = ", wallet[c].balance)
        print()
