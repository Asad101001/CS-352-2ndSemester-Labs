from factor_demo import FactorDemo


def main():
    obj = FactorDemo(12)

    print("\n CASE 1: Modern 'return' in generator (StopIteration.value demo):")
    g = obj.bad_generator_mix()
    while True:
        try:
            print(next(g))
        except StopIteration as e:
            print("Generator stopped. Hidden returns value", e)
            break

    print("\n CASE 2: Logical error (compiles but wrong behaviour)")
    for x in obj.bad_generator_logic():
        print(x)

    print("\n CASE 3: Correct generator")
    for x in obj.good_generator():
        print(x)


if __name__ == "__main__":
    main()


#  CASE 1: Modern 'return' in generator (StopIteration.value demo):
# 1
# 2
# 3
# 4
# 6
# Generator stopped. Hidden returns value Too big

#  CASE 2: Logical error (compiles but wrong behaviour)
# [1]
# [1, 2]
# [1, 2, 3]
# [1, 2, 3, 4]
# [1, 2, 3, 4, 6]
# [1, 2, 3, 4, 6, 12]

#  CASE 3: Correct generator
# 1
# 2
# 3
# 4
# 6
# 12
