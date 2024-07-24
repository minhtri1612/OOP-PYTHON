class A:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __mul__(self,other):
        x=self.x*other.x
        y=self.y*other.y
        a3=A(x,y)
        return a3
a1=A(7,2)
a2=A(3,4)
a3=a1*a2
print(a3.x,a3.y)