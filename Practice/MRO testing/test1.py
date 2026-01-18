class A:
    def whoami(self):
        return "A"


class B(A):
    def whoami(self):
        return "B"


class C(B):
    def whoami(self):
        return "C"


def describe(obj: A):
    print("Type", type(obj).__name__)
    print("Who am I?", obj.whoami())


x = C()
describe(x)
print(C.__mro__)


##  Type C
##  Who am I? C

## REASONING:
##  MRO-> (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
