class Course:
    def __init__(self,code,course_name):
        self.code=code
        self.course_name=course_name
    
    def describe(self):
        print(f" Course code={self.code},name={self.course_name}")
        
class Student:
    def __init__(self,name,id,code,course_name):
        self.name=name
        self.id=id
        self.khoa_hoc=Course(code,course_name)
        
    def describe(self):
        print(f"name=:{self.name},student id:{self.id}")
        self.khoa_hoc.describe()
hoc_sinh =Student("david",1344,246,"minh tri")
hoc_sinh.describe()