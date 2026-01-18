class ChangeCalculator:
    def __init__(self, charged_amount, given_amount):
        self.__amount_charged = charged_amount
        self.__amount_given = given_amount
        self.__denominations = (5000, 1000, 500, 100, 50, 20, 10, 5, 2, 1)

    @property
    def denominations(self):
        return self.__denominations

    @property
    def amount_charged(self):
        return self.__amount_charged

    @amount_charged.setter
    def amount_charged(self, value):
        self.__amount_charged = value

    @property
    def amount_given(self):
        return self.__amount_given

    @amount_given.setter
    def amount_given(self, value):
        self.__amount_given = value

    @property
    def change(self):
        remaining = self.__amount_given - self.__amount_charged
        breakdown = {}

        for denom in self.__denominations:
            if remaining <= 0:
                break
            count = remaining // denom
            if count:
                breakdown[denom] = count
                remaining %= denom
        return breakdown

    def _format_denomination(self, denom, qty):
        unit = "note/s" if denom >= 10 else "coin/s"
        return f" {qty} {unit} of {denom}"

    def _format_change_string(self):
        change = self.change
        if not change:
            return "no change"
        items = [self._format_denomination(d, q) for d, q in change.items()]
        return (
            "You have" + "".join(items[:-1] + [f"{items[-1]}."])
            if len(items) > 1
            else items[0] + "."
        )

    def display_change(self):
        print(self._format_change_string())

    def __str__(self):
        return (
            f"Charged Amount: {self.__amount_charged}\n"
            f"Given Amount: {self.__amount_given}\n"
            f"Cash Back: {self._format_change_string()}"
        )


# === VALIDATORS ONLY (optional) ===
def _validate_int(name, value, min_val=0):
    if not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value < min_val:
        raise ValueError(f"{name} cannot be negative")
    return value


def _charged_amount_validator(self, charged, given):
    charged = _validate_int("charged_amount", charged)
    if charged > given:
        raise ValueError("charged_amount cannot exceed given_amount")
    return charged


def _given_amount_validator(self, given, charged):
    given = _validate_int("given_amount", given)
    if given < charged:
        raise ValueError("given_amount cannot be less than charged_amount")
    return given


# ==================================
