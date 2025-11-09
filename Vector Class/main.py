from vector import Vector

v = Vector(5)
v[1] = 69
v[-1] = 420

print(v)
print(v[4])

u = v + v
print(u)

total = 0
for entry in v:
    total += entry
