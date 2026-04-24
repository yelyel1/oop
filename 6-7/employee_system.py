class Employee:
    def __init__(self, name):
        self.__name = name
        self.__salary = 0
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
    def get_salary(self):
        return self.__salary

emp = Employee("MARLYN")
emp.set_salary(30000)
print("Salary:", emp.get_salary())
#MGM