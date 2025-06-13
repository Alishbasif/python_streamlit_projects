class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
       return print(f"A {self.name} of breed {self.breed} says woof!")

d1 = Dog("Tommy", "Asian")
print(d1.bark())

