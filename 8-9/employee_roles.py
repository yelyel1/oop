class Employee:
    def work(self):
        print("Employee performs tasks")

class Programmer(Employee):
    def work(self):
        print("Programmer writes code")

class Designer(Employee):
    def work(self):
        print("Designer creates UI designs")

employees = [Programmer(), Designer()]
for emp in employees:
    emp.work()
    #MGM