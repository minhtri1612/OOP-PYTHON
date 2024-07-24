class DATE:
    def __init__(self,day,month,year):
        self.day=day
        self.month=month
        self.year=year
    def describe(self):
        print(f"day:{self.day},month:{self.month},year:{self.year}")

class Book:
    def __init__(self,name,author,day,month,year):
        self.name=name
        self.author=author
        self.publication_date=DATE(day,month,year)
        
    def describe(self):
        print(f"Booke name:{self.name},Author name:{self.author}")
        self.publication_date.describe()
        
sach= Book("C++","Peter",27,6,2002)
sach.describe()