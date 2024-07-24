from statistics import mean

class Student:
    def __init__(self,hs_name,hs_year,hs_grade):
        self.hs_name=hs_name
        self.hs_year=hs_year
        self.hs_grade=hs_grade
    
    def describe(self):
        print(f"student name:{self.hs_name},student year:{self.hs_year},student grade:{self.hs_name}")
        
class Teacher:
    def __init__(self,te_name,te_year,te_subject):
        self.te_name=te_name
        self.te_year=te_year
        self.te_subject=te_subject
    
    def describe(self):
        print(f"teacher name:{self.te_name},teacher year of birth:{self.te_year},teacher's subject:{self.te_subject}")
        
        
class Doctor:
    def __init__(self,doc_name,doc_year,doc_specialist):
        self.doc_name=doc_name
        self.doc_year=doc_year
        self.doc_specialist=doc_specialist
        
    def describe(self):
        print(f"Doctor name is:{self.doc_name},Doctor year is:{self.doc_year},Doctor's specialist:{self.doc_specialist}")

    def countDoctor(self):
        return sum(1 for person in self.people if isinstance(person, Doctor))

    def sortAge(self):
        self.people.sort(key=lambda person: person.hs_year if isinstance(person, Student) else person.te_year if isinstance(person, Teacher) else person.doc_year)

    def aveTeacherYearOfBirth(self):
        teacher_years = [person.te_year for person in self.people if isinstance(person, Teacher)]
        return mean(teacher_years) if teacher_years else None
    
class Ward:
    def __init__(self,Ward_name):
        self.Ward_name=Ward_name
        self.people=[]
    def addPerson(self,person):
        self.people.append(person)
    def describe(self):
        print("Ward name is:",self.Ward_name)
        print("information of the Ward:")
        for i in self.people:
            i.describe()
phuong=Ward("gentleman")
hocsinh1=Student("minh tri",2003,4)
giaovien1=Teacher("Van",2233,"math")
giaovien2=Teacher("Tung",345,"English")
bacsi1=Doctor("Dat",234,"Heart")
bacsi2=Doctor("vc",245,"tim mach")
phuong.addPerson(hocsinh1)
phuong.addPerson(giaovien1)
phuong.addPerson(giaovien2)
phuong.addPerson(bacsi1)
phuong.addPerson(bacsi2)
phuong.describe()
phuong.describe()
print("\nNumber of doctors:", phuong.countDoctor())

phuong.sortAge()
print("\nSorted by age:")
phuong.describe()

average_year = phuong.aveTeacherYearOfBirth()
print("\nAverage year of birth of teachers:", average_year if average_year is not None else "No teachers in the ward")
