'''
class have two types of relation
1. is-a relation: it is a relationship between two classes where one class is a subclass of another class. use inheritance to implement this relation.
2. has-a relation: it is a relationship between two classes where one class contains an instance of another class as a member variable.
'''

# is-a relation
# use super keyword to call the parent class constructor and initialize the parent class attributes in the child class constructor  
class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal called...")
    def sound(self):
        print("some generic sound...")

class Dog(Animal):
    def __init__(self, name):
        print(f"{name} called...")
        super().__init__(name) # calling the parent class constructor
    def sound(self):
        print(f"{self.name} barks...")

dog = Dog("Tommy")
dog.sound()

# has-a relation
class Engine:
    def __init__(self, power):
        self.power = power
        print("Engine called...")

class Car:
    def __init__(self):
        self.engine = Engine(100) # Car has an Engine
        print("Car called...")

car = Car()