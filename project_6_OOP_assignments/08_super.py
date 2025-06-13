class Person:

    def __init__(self,name):
        self.name = name

class Teacher(Person):

    def __init__(self, name, subfield):
        super().__init__(name) 
        self.subfield = subfield    

t1 = Teacher("Alishba", "BS-IT")
print(t1.name, t1.subfield)