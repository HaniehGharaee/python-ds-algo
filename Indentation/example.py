class ExampleClass:
    def __init__(self):
        self.name = "example"
    def someFunction(self, a):
        if a > 5:
            return True
        else:
            return False
obj = ExampleClass() # Creating an object (instance)
print(obj.name) #Access to property
#Calling the method
print(obj.someFunction(10))
print(obj.someFunction(3))
        
def separateFunction(b):
    for i in b:
        if i == 1:
            return True
    return False
print(separateFunction([2,3,5,6,1]))
print(separateFunction([2,3,5,6,0]))
