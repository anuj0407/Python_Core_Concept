#OOPs (Object-Oriented Programming) in Python 
#Class: A class is a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have.
#Object: An object is an instance of a class. It is created from the class and has the attributes and methods defined in the class.

class Computer:
    def  __init__(self,brand,model,price):#constructor method
        print(f"Computer class constructor")
        self.brand = brand
        self.model = model
        self.price = price
    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}")

#Creating objects of the Computer class
comp1 = Computer("Dell", "XPS 13", 999.99)
comp1.display() 
comp2 = Computer("Apple", "MacBook Pro", 1299.99)
comp2.display()
print(type(comp1)) # output: <class '__main__.Computer'>
