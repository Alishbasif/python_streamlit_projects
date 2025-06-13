def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet 
    return cls



@add_greeting
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age



p1 = Person("AlishbaAsif", 20)
print(p1.greet())
print(f"The student {p1.name} is {p1.age} years old.")









