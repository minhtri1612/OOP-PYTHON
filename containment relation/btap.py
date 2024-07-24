# Write a function to check if two people have the same name.

# Write a function to check if two people have the same date of birth
class Date:
    def __init__(self,day,month,year):
        self.day=day
        self.month=month
        self.year=year
        
    def same_day_of_birth(self,other):
        return (self.day==other.day) and (self.month==other.month) and (self.year==other.year)
    
    def display(self):
        print(f"ngay: {self.day} thang: {self.month} nam: {self.year}")
