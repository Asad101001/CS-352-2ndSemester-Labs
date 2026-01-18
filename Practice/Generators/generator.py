# slower because brute force checks
def factor_gen_slow(n):
    for k in range(1, n + 1):
        if n % k == 0:
            yield k


print("\tFactors generator slow")
for i, f in enumerate(factor_gen_slow(1000000)):
    if i > 50:
        break
    print(i, f)


# faster because it only checks pair of uptil sqrt(n)
def factor_gen_fast(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:  # perfect square
        yield k


print("\tFactors generator fast")
for i, f in enumerate(factor_gen_fast(1000000)):
    if i > 50:
        break
    print(i, f)
