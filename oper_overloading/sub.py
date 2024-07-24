class A:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __sub__(self,other):
        x=self.x-self.y
        y=other.x-other.y
        a3=A(x,y)
        return a3
a1=A(1,2)  #self
a2=A(3,4)  #other
a3=a1-a2
print(a3.x,a3.y)