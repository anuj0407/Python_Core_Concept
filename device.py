# Dunder method is a special method in Python that starts and ends with double underscores (__) and is used to define the behavior of an object when certain operations are performed on it. Dunder methods are also known as magic methods or special methods.
# __init__ is a dunder method that is called when an object is created from a class. It is used to initialize the attributes of the object.

class Device:
    def __init__(self,name):
        print("init called for: ", name)
        self.name = name.upper()

    def display(self):
        print("Device: ",self.name)

device1 = Device("laptop")
device2 = Device("mobile")

device1.display()
device2.display()

