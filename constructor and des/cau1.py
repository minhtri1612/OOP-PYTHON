class Employee:
  def __init__(self):
    print("employee called")
  def __del__(self):
    print("employee deleted")
  def hello(self):
    print("hello")
a=Employee()

def Create_obj():
    print('Making Object...')
    obj = Employee()
    print('function end...')
    return obj

print('Calling Create_obj() function...')
obj = Create_obj()
a=Employee()
print('Program End...') 
del a
