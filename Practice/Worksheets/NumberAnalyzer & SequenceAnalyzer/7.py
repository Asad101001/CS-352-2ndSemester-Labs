class NumberAnalyzerV2:
    def __init__(self, value):
        value = value + 1
        self.value = value


x = NumberAnalyzerV2(4)
print(value)

##  NameError: name 'value' is not defined. Did you mean: 'False'?
##  Error: value not defined (should've provided an instance : "print(x.value)")
