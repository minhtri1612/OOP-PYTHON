class DATE:
    def __init__(self,day,month,year):
        self.day=day
        self.month=month
        self.year=year
    def describe(self):
        print(f"day:{self.day},month:{self.month},year:{self.year}")

class Book:
    def __init__(self,name, author,date):
        self.name=name
        self.author=author
        self.obj_date=date
    def describe(self):
        print(f"Booke name:{self.name},Author name:{self.author}")
        self.obj_date.describe()
publicationDate=DATE(27,6,2022)
book =Book("C++","Peter",publicationDate)
book.describe()
