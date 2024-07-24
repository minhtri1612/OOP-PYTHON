class Student:
    def __init__(self,m1,m2):
       self.m1=m1
       self.m2=m2
    
    def __gt__(self,other):
        r1=self.m1+self.m2
        r2=other.m1+other.m2
        if r1>r2:
            return True
        else:
            return False
a1=Student(2,4)#self
a2=Student(3,1)#other

if a1>a2:
  print("a1 wins")
else:
  print("a2 wins")
