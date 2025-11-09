class Vector:

    def __init__(
        self, d=2
    ):  # Default null constructor initiates 2d vector unless dimensions input as parameters
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, index):
        return self._coords[index]

    def __setitem__(self, index, value):
        self._coords[index] = value

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Number of dimensions must be same")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self) -> str:
        return "<" + str(self._coords)[1:-1] + ">"
