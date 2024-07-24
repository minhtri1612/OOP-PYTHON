import copy
class Shallow_copy:
    def __init__(self,data):
        self.data=data
    
    def __str__(self):
        return f"original data:{self.data}"
    
    def shallow_copy(self):
        return copy.copy(self)
    
original_obj=Shallow_copy([1,2,3])
copy_obj=original_obj.shallow_copy()
print(original_obj)
print(copy_obj)
original_obj.data.append(8)
print(original_obj)
print(copy_obj)
copy_obj.data.append(4)
print(original_obj)
print(copy_obj)