from abc import ABC ,abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self,length,height):
        self.length = length
        self.height = height

    def area(self):
        area = self.length * self.height
        return print(f"The area of a reactangle is : {area}")

r1 = Rectangle(4,8)
print(r1.area())
