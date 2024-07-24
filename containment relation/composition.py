class Salary:
    def __init__(self,bonus,pay):
        self.bonus=bonus
        self.pay=pay
    
    def annual_salary(self):
        return (self.bonus*2)+self.pay
    
class Employee:
    def __init__(self,name,age,bonus,pay):
        self.name=name
        self.age=age
        self.obj_salary=Salary(bonus,pay)
    def total_salary(self):
        return self.obj_salary.annual_salary()
    
emp=Employee("John",25,1500,400)
print(emp.total_salary())


# # include <iostream>
# # include <string>
# using namespace std;

# class Salary {
# private:
#     double pay;
#     double bonus;
# public:
#     Salary(double pay, double bonus) {
#         this->pay = pay;
#         this->bonus = bonus;
#     }
#     double annual_salary() const {
#         return (pay * 12) + bonus;
#     }
# };

# class Employee {
# private:
#     string name;
#     int age;
#     Salary* obj_salary;
# public:
#     Employee(string name, int age, Salary* salary) {
#         this->name = name;
#         this->age = age;
#         this->obj_salary = salary;
#     }
#     double total_salary() const {
#         return obj_salary->annual_salary();
#     }
# };

# int main() {
#     Salary salary(200, 300);
#     Employee emp("John", 25, &salary);
#     cout << emp.total_salary() << endl;
#     cout << salary.annual_salary() << endl;
#     return 0;
# }