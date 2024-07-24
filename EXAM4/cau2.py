class Beverage:
    def __init__(self,price=0.0, topping_price=0.0,condiment_price=0.0):
        self.__price=float(price)
        self.__topping_price=float(topping_price)
        self.__condiment_price=float(condiment_price)
        
    def set_price(self,price):
        self.__price=price
    def get_price(self):
        return self.__price
    
    def set_topping_price(self,topping_price):
        self.__topping_price=topping_price
    def get_topping_price(self):
        return self.__topping_price
    
    def set_condiment_price(self,condiment_price):
        self.__condiment_price=condiment_price
    def get_condiment_price(self):
        return self.__condiment_price
    
    def __eq__(self,other):
        return(self.__price == other.__price and
            self.__topping_price == other.__topping_price and
            self.__condiment_price == other.__condiment_price) 
    
    def __copy__(self):
        return Beverage(self.__price,self.__topping_price,self.__condiment_price)
    
    def __add__(self,other):
        m1=self.__price+other.__price
        m2=self.__topping_price+other.__topping_price
        m3=self.__condiment_price+other.__condiment_price
        return Beverage(m1,m2,m3)
    
    def describe(self):
        print(f"price:{self.__price}, topping price:{self.__topping_price},condiment price:{self.__condiment_price}")
b0=Beverage()
b0.describe()
b1=Beverage(10.5,2.3,1.2)
b1.describe()
b2=Beverage(15,2.2,0.5)
b2.describe()
b3=b1.__copy__()
b3.describe()
b4=b1+b2
b4.describe()
print("is b3=b1?",(b3==b1))