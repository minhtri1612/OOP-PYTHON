from abc import ABC, abstractmethod
class Point:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
    def setX(self,x):
        self.__x=x
    def getX(self):
        return self.__x
    def setY(self,y):
        self.__y=y
    def getY(self):
        return self.__y
    
class TwoDShape:
    def __init__(self,x,y):
        self.center_point=Point(x,y)
     
    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def double_perimeter(self):
        pass
    
    @abstractmethod
    def double_area(self):
        pass

    @abstractmethod
    def display(self):
        pass

class Circle(TwoDShape):
    def __init__(self,radius,x,y):
        super().__init__(x, y)
        self.radius=radius
    def double_perimeter(self):
        return self.radius*self.radius
    def double_area(self):
        return self.radius*2
    def display(self):
        print("perimeter of Circle:{0},area of Circle:{1},,x:{2},y:{3}".format(self.double_perimeter(),self.double_area(),self.center_point.getX(),self.center_point.getY()))
    
class Rectangle(TwoDShape):
    def __init__(self,width,height,x,y):
        super().__init__(x, y)
        self.width=width
        self.height=height
    def double_perimeter(self):
        return (self.width+self.height)*2
    def double_area(self):
        return self.width*self.height
    def display(self):
        print("perimeter of Rectangle:{0},area of Rectangle:{1},x:{2},y:{3}".format(self.double_perimeter(),self.double_area(),self.center_point.getX(),self.center_point.getY()))
    
    
class Square(TwoDShape):
    def __init__(self,side,x,y):        
        super().__init__(x, y)
        self.side=side
    def double_perimeter(self):
        return self.side*4
    def double_area(self):
        return self.side*self.side
    def display(self):
        print("perimeter of Square:{0},area of Square:{1},x:{2},y:{3}".format(self.double_perimeter(),self.double_area(),self.center_point.getX(),self.center_point.getY()))
    
rect = Rectangle(10, 5, 2, 3)
rect.display()
print("Perimeter:", rect.double_perimeter())
print("Area:", rect.double_area())

square = Square(4, 1, 1)
square.display()
print("Perimeter:", square.double_perimeter())
print("Area:", square.double_area())