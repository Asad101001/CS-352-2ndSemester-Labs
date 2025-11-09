class Range:

    def __init__(self, start, stop=None, step=1) -> None:
        if step == 0:
            raise ValueError("Step taken cannot be zero")
        if stop is None:
            start, stop = 0, start
        self._length = max(0, (stop - start + step - 1) // step)
        self._start = start
        self._step = step
        self._stop = stop

    def __len__(self):
        return self._length

    def __getitem__(self, index):
        if index < 0:
            index += len(self)
        if not 0 <= index < self._length:
            raise IndexError("Index out of range!")

        return self._start + index * self._step
    
    def __str__(self) -> str:
        return f"Range ({self._start},{self._stop},{self._step})"

