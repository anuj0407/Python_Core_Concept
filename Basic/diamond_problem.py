# multiple inheritance and the diamond problem
'''
Diamond problem occurs when a class inherits from two classes that both inherit from a common base class.
This can lead to ambiguity because the derived class may not know which version of the base class's methods or attributes to use.

It occurs in many other languages like java but Python uses a MRO(Method Resolution Order) to resolve this issue. 
The MRO is a linearization of the class hierarchy that determines the order in which methods are resolved when they are in multiple inheritance.
'''

class parentA:
    def __init__(self):
        print("parentA called...")

class parentB(parentA):
    def __init__(self):
        print("parentB called...")
        super().__init__() #calling the next class in the MRO or calling the parent class 

class parentC(parentA):
    def __init__(self):
        print("parentC called...")
        super().__init__() #calling the next class in the MRO or calling the parent class
    
class child(parentB, parentC):
    def __init__(self):
        print("child called...")
        super().__init__() #calling the next class in the MRO or calling the parent class

# obj = child()
for cls in child.mro():
    print(cls)