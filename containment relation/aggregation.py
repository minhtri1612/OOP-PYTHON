class Salary:
    def __init__(self,bonus,pay):
        self.bonus=bonus
        self.pay=pay
    
    def annual_salary(self):
        return (self.bonus*12)+self.pay
    
class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.obj_salary=salary
    def total_salary(self):
        return self.obj_salary.annual_salary()
salary = Salary(200, 300)
emp = Employee("John", 25, salary)
obj_salary = salary.annual_salary()

print(emp.total_salary())  # Output: 2700
print(obj_salary)          # Output: 2700