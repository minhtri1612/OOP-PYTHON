import copy
class DeepCopy:
    def __init__(self,data):
        self.data=data
        
    def __str__(self):
        return f"original object:{self.data}"
    
    def deepcopy(self):
        return copy.deepcopy(self)
    
original_object = DeepCopy([1, [2, 3], 4])
copy_object = original_object.deepcopy()

print(original_object)
print(copy_object)

original_object.data[1].append(99)
print(original_object)
print(copy_object)

copy_object.data[1].append(23)
print(original_object)
print(copy_object)