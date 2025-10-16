#R-1.1 Write a short Python function, is multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.

n = input ("Enter an integer 'n'")
m = input ("Enter an integer 'm'")
i=0
match = False

while not n == m*i:
 if n == m*i:
  print("n is a multiple of m at integer {i}")
  match = True
  break
 else:
  i += 1
