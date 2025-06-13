class Employee:

    def __init__(self, name, salary,):
        self.name = name
        self._salary = salary
        self.__ssn = "scbyt52"


    def get_attr(self):
        return self.__ssn    


e1 = Employee("Alishba", 100000,)
print(e1.name)
print(e1._salary)          # not prefer!
print(e1.get_attr())

