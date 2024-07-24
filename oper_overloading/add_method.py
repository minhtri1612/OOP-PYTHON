class Student:
    def __init__(self, m1, m2):
        self.__m1 = m1
        self.__m2 = m2
    
    def __add__(self, other):
        m1 = self.__m1 + other.__m1
        m2 = self.__m2 + other.__m2
        s3 = Student(m1, m2)
        return s3
    
    def __str__(self):
        return "{} {}".format(self.__m1, self.__m2)
    
    def get_marks(self):
        return self.__m1, self.__m2
    
a1 = Student(50, 60)
a2 = Student(45, 23)
a3 = a1 + a2

# Accessing the private members using a method
m1, m2 = a3.get_marks()
print(m1, m2)
print("gia tri cua a1:", a1)
print("gia tri cua a2:", a2)
