class A:
    def __init__(self) -> None:
        print("A")


class B(A):
    def __init__(self) -> None:
        print("B")
        super().__init__()


class C(A):
    def __init__(self) -> None:
        print("C")
        super().__init__()


class D(B, C):
    def __init__(self) -> None:
        print("D")
        super().__init__()


d = D()

## D
## B
## C
## A
