# class Person{
#     private:
#     string name;
#     Date birthOfDate;
#     public:
#     Person(string name,  Date birthOfDate):birthOfDate(birthOfDate){
#         this->name=name;
#     }
#     void  display(){
#         cout<<name;
#         birthOfDate.display();
#     }
# };

# int main(){
#     Date a(16,12,2004);
#     Person tri("tri",a);
#     tri.display();
# }```

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
    a = Date(16, 12, 2004)
    tri = Person("tri", a)
    tri.display()