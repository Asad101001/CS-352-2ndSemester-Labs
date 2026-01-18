from rational_number import RationalNumber

r1 = RationalNumber(1, 6)
r2 = RationalNumber(4, 7)

print("Rational number addition")
r3 = r1 + r2
print("\t\t",r3)

print("Rational number subtraction")
r4 = r1 - r2
print("\t\t",r4)

print(r1.GCD(18, 36))

print(r1.LCM(18, 36))
