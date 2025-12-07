class P31:
    def __init__(self, charged, given):
        self._charged = charged
        self._given = given
        self._denominations = {
            "1000 pkr bill": 1000,
            "500 pkr bill": 500,
            "100 pkr bill": 100,
            "50 pkr bill": 50,
            "20 pkr bill": 20,
            "10 pkr bill": 10,
            "5 pkr coin": 5,
            "2 pkr coin": 2,
            "1 pkr coin": 1,
            "0.5 paisa coin": 0.5
        }

    def make_change(self):
        try:
            self._charged = float(self._charged)
            self._given = float(self._given)

            if self._charged < 0 or self._given < 0:
                raise ValueError("Amounts cannot be negative.")

            if self._given < self._charged:
                return "Insufficient amount given."

            change = round(self._given - self._charged, 2)

            result = {}
            for name, value in self._denominations.items():
                count = int(change // value)
                if count > 0:
                    result[name] = count
                    change -= count * value

            return result

        except ValueError as ve:
            return f"ValueError: {ve}"
        except TypeError:
            return "TypeError: Inputs must be numbers."
        except Exception as e:
            return f"Unexpected Error: {e}"
