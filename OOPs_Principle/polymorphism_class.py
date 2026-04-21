'''
Polymorphism is another one principle of OOPs
Poly means many and morphism means forms. Polymorphism allows objects of different classes to be treated as objects of a common superclass. It is the ability of an object to take on many forms.
polymorphism is of two types:
1. Compile-time polymorphism (method overloading): It is the ability to define multiple methods with the same name but different parameters in the same class. The method to be called is determined at compile time based on the number and type of arguments passed.
since python is dynamically typed and does not support method overloading, we can achieve it by using default arguments or variable-length arguments in a single method definition.
2. Run-time polymorphism (method overriding): It is the ability of a subclass to provide a specific implementation of a method that is already defined in its superclass. The method to be called is determined at runtime based on the type of the object.
'''

# Compile-time polymorphism (method overloading) using default arguments
class Calculator:
    def add(self, a = 5, b = 10):
        return a+b
    
calc = Calculator()
print(calc.add(2,5)) #both arguments provided
print(calc.add(3)) #single argument provided, b will take default value 10
print(calc.add()) #no arguments provided, a and b will take default values 5 and 10 respectively


# Run-time polymorphism (method overriding)
class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print("Some generic sound")

class Dog(Animal):
    def sound(self): #overriding the sound method of the parent class
        print(f"{self.name} barks!")

class Cat(Animal):
    def sound(self): #overriding the sound method of the parent class
        print(f"{self.name} meows!")

dog1 = Dog("Bob")
cat1 = Cat("Alice")
dog1.sound() # method of Dog class will be called
cat1.sound() # method of Cat class will be called
