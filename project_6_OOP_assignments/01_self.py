class Student:

    def __init__(self,name:str,marks:int):
        self.name = name
        self.marks =  marks

    def display(self):
        print( f"{self.name} has {self.marks} marks.")   

s1 = Student("Alishba" , 98)
s1.display()