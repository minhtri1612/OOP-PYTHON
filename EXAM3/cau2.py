class Product:
    def __init__(self,price=0.0,weight=0.0,discount=0.0):
        self.__price=price
        self.__weight=weight
        self.__discount=discount
    
    def __copy__(self):
        return Product(self.__price,self.__weight,self.__discount)
    def get_price(self):
        return self.__price

    def get_weight(self):
        return self.__weight

    def get_discount(self):
        return self.__discount

    def set_price(self, price):
        self.__price = float(price)

    def set_weight(self, weight):
        self.__weight = float(weight)

    def set_discount(self, discount):
        self.__discount = float(discount)

    def describe(self):
        print(f"Price: {self.__price}, Weight: {self.__weight}, Discount: {self.__discount}")

    def __add__(self,other):
        m1=self.__price+other.__price
        m2=self.__weight+other.__weight
        m3=self.__discount+other.__discount
        return Product(m1,m2,m3)

    def __eq__(self,other):
        return (self.__price == other.__price and
                self.__weight == other.__weight and
                self.__discount == other.__discount
            )
product1 = Product()
product1.describe()

product2 = Product(50.0, 2.5, 10.0)
product2.describe()

product2.set_price(55.0)
product2.set_weight(2.8)
product2.set_discount(12.0)
product2.describe()
product3=product2+product1
product3.describe()
product4=product1.__copy__()
product4.describe()
print(product1==product2)
print(product1==product4)

