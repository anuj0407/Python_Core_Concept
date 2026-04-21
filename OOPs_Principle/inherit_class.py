# Inheritance is one of the OOPs principle 
# Inheritance is a concept that allows a new class (called a child class or subclass) to inherit attributes and methods from an existing class (called a parent class or superclass).
# The child class can also have its own attributes and methods, and it can override the methods of the parent class.

#parent class 
class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"Animal Name: {self.name}")

    def sound(self):
        print("Some generic sound")

#child class
class Dog(Animal):
    def sound(self): #overriding the sound method of the parent class
        print(f"{self.name} barks!") 

dog1 = Dog("Bob")
dog1.info() # parent class method
dog1.sound() # child class overridden method
