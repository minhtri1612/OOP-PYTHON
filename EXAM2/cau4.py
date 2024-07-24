class IceCream:
    def __init__(self,ice_price,topping_price,flavor_price):
        self.__ice_price=float(ice_price)
        self.__topping_price=float(topping_price)
        self.__flavor_price=float(flavor_price)
        
    def set_ice(self, ice_price):
        self.__ice_price = ice_price

    def get_ice(self):
        return self.__ice_price

    def get_topping(self):
        return self.__topping_price

    def get_flavor(self):
        return self.__flavor_price

    def __copy__(self):
        return IceCream(self.__ice_price, self.__topping_price, self.__flavor_price)
    
    def __sub__(self,other):
        ice_price=self.__ice_price-other.__ice_price
        topping_price=self.__topping_price - other.__topping_price
        flavor_price =self.__flavor_price - other.__flavor_price
        return IceCream(ice_price, topping_price, flavor_price)


    def describe(self):
        print(f"ice price:{self.__ice_price},topping price:{self.__topping_price},flavor price:{self.__flavor_price}")
    
    def __le__(self, other):
        return (self.__ice_price <= other.__ice_price and
                self.__topping_price <= other.__topping_price and
                self.__flavor_price <= other.__flavor_price)
    
    def __eq__(self,other):
        return (self.__ice_price == other.__ice_price and
                self.__topping_price == other.__topping_price and
                self.__flavor_price == other.__flavor_price)
        
ic0 = IceCream(10.5, 2.3, 1.2)
ic0.describe()

ic1 = ic0.__copy__()
ic1.describe()

ic2=IceCream(15,1,0.5)
ic2.describe()
ic3=ic2-ic1
ic3.describe()
print(ic0 <= ic3)  
print(ic1 <= ic0)
print(ic0==ic1)
print(ic0 == ic3)  
