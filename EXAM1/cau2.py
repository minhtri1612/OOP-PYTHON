class Complex:
    def __init__(self, real=0.0, imag=0.0):
        self.__real = float(real)
        self.__imag = float(imag)

    def __copy__(self):
        return Complex(self.__real, self.__imag)

    def __add__(self,other):
        real=self.__real+other.__real
        imag=self.__imag +other.__imag
        s3=Complex(real,imag)
        return s3
    
    def __eq__(self,other):
        A=self.__real+self.__imag
        B=other.__real +other.__imag
        if A==B:
            return True
        else:
            return False
    
    def get_marks(self):
        return self.__real,self.__imag
        
        
A=Complex(2,4) #self
B=Complex(1,5) #other
s3=A+B
real , imag =s3.get_marks()
print(real,imag)
if A==B:
    print("A equal to B")
else:
    print("A not equal to B")