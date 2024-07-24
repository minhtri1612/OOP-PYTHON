class Manufacturer:
    def __init__(self,id,location):
        self.id=id
        self.location=location
        
    def describe(self):
        print(f"id={self.id} and location={self.location}")
        
class Device:
    def __init__(self,name,price,id,location):
        self.name=name
        self.price=float(price)
        self.manu=Manufacturer(id,location)
    def describe(self):
        print(f"name={self.name} and price={self.price}")
        self.manu.describe()
        
manu=Manufacturer(9725,"VietNam")
mouse=Device("mouse",2.5,9725,"VietNam")
mouse.describe()