class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    def display_manager(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)

manager1 = Manager("MARLYN", 50000, "IT")
manager1.display_manager()
#MGM