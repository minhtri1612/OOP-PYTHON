class Course:
    def __init__(self,code,course_name):
        self.code=code
        self.course_name=course_name
    
    def describe(self):
        print(f"Course code={self.code},name={self.course_name}")
        
class Student:
    def __init__(self,name,id,khoa_hoc):
        self.name=name
        self.id=id
        self.khoa_hoc=khoa_hoc
    
    def describe(self):
        print(f"name=:{self.name},student id:{self.id}")
        self.khoa_hoc.describe()
        
khoa_hoc=Course(246,"minh tri")
hoc_sinh=Student("tri",355,khoa_hoc)
hoc_sinh.describe()