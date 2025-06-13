class Multiplier:

    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        self.factor *= value
        return f"The factor is {self.factor}."
    

m1 = Multiplier(5)
print(m1(4))
print(callable(m1))