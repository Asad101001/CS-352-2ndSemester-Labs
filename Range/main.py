from range import Range

r1 = Range(2, 10, 2)
r2 = Range(0, 30, 5)
r3 = Range(6)
r4 = Range(30, 5, -4)

print(len(r1))
print(len(r2))
print(len(r3))
print(len(r4))

print(f"Elements in ", r1, [r1[n] for n in range(len(r1))])

print(f"Elements in ", r2, [r2[n] for n in range(len(r2))])

print(f"Elements in ", r3, [r3[n] for n in range(len(r3))])

print(f"Elements in ", r4, [r4[n] for n in range(len(r4))])
