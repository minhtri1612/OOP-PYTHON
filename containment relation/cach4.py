# class Person{
#     private:
#         string name;
#         Date* dateOfBirth;

#     public:
#         Person(string name, int day, int month, int year) {
#             this->name = name;
#             this->dateOfBirth = new Date(day, month, year);
#         }
#         void display(){
#             cout<<name;
#             dateOfBirth->display();
#         }
# };

# int main() {
#     Person peter("peter", 10, 1, 2000);
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
    def __init__(self,name,day,month,year):
        self.name=name
        self.date_of_birth=Date(day, month, year)
    def display(self):
        print(self.name, end=' ')
        self.date_of_birth.display()

if __name__ == "__main__":
    peter = Person("peter", 10, 1, 2000)
    peter.display()

