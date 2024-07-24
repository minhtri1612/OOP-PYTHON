# class Person{
#     private:
#         string name;
#         Date& dateOfBirth;

#     public:
#         Person(string name, Date& dateOfBirth):dateOfBirth(dateOfBirth) {
#             this->name = name;
#         }
#         void display(){
#             cout<<name;
#             dateOfBirth.display();
#         }

# };

# int main() {
#     Date date(10, 1, 2000);
#     Person peter("peter", date);
#     peter.display();
# }```

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"{self.day}/{self.month}/{self.year}")

class Person:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    def display(self):
        print(self.name, end=' ')
        self.date_of_birth.display()

if __name__ == "__main__":
    date = Date(10, 1, 2000)
    peter = Person("peter", date)
    peter.display()

