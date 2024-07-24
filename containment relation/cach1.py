# class Date{
# private:
# int day;
# int month;
# int year;
# public:
# Date(int day, int month, int year){
#     this->day=day;
#     this->month=month;
#     this->year=year;
# }
# void display(){
#     cout<<day<<"/"<<month<<"/"<<year;
# }
# };
# class Person{
#     private:
#     string name;
#     Date dateofBirth;
#     public:
#     Person(string name,int day, int month, int year):dateofBirth(day,month, year){
#         this->name=name;
#     }
#     void display(){
#         cout<<name;
#         dateofBirth.display();
#     }
# };

# int main(){
#     Date a(16,12,2004);
#     Person tri("tri",16,12,2004);
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
    def __init__(self,name,day,month, year):
        self.name=name
        self.date_of_birth=Date(day, month, year)
        
    def display(self):
        print(self.name,end="")
        self.date_of_birth.display()
if __name__ == "__main__":
    a = Date(16, 12, 2004)
    tri = Person("tri", 16, 12, 2004)
    tri.display()