# class Person {
# private:
#     string name;
#     Date* dateOfBirth;
# public:
#     Person(string name, Date* dateOfBirth) : name(name), dateOfBirth(dateOfBirth) {}
#     void display() const {
#         cout << "Name: " << name << ", Date of Birth: ";
#         dateOfBirth->display();
#     }
# };

# int main() {
#     Date date(10, 1, 2000);
#     Person peter("peter", &date);
#     peter.display();
#     return 0;
# }

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"{self.day}/{self.month}/{self.year}")
   
class Person:
    def __init__(self,name,date_of_birth):
        self.name=name
        self.date_of_birth=date_of_birth
    def display(self):
        print(self.name)
        self.date_of_birth.display()
if __name__ == "__main__":
    date = Date(10, 1, 2000)
    peter = Person("peter", date)
    peter.display()