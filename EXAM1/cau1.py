class Employee:
    def __init__(self,id,name,gender,depar_id):
        self.__id=id
        self.__name=name
        self.__gender=gender
        self.__depar_id=depar_id
        
    def setname(self,name):
        self.__name=name
    
    def getname(self):
        return self.__name

    def setid(self,id):
        self.__id=id

    def getid(self):
        return self.__id
    
    def setgender(self,gender):
        self.__gender=gender
    
    def getgender(self):
        return self.__gender    
    
    def set_departid(self,depar_id):
        self.__depar_id=depar_id
    
    def get_departid(self):
        return self.__depar_id

    def display(self):
        print("{0} {1} {2} {3}".format(self.__name,self.__id,self.__gender,self.__depar_id))
        
class Manager(Employee):
    pass

A=Employee(23,"minh tri","nam",1612)
B=Manager(45,"hoang","nu",6543)
A.display()
B.display()