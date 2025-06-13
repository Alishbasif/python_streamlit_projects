class Department:

    def __init__(self, name):
        self.name = name

class Employee:

    def __init__(self, employee_name,department):
        self.employee_name = employee_name
        self.department = department


d1 = Department("IT department")
print(d1.name)
e1 = Employee("Alishba", d1)
print(f"{e1.employee_name} is doing job at {e1.department.name}")
