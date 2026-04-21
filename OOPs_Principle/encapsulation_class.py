'''
Encapsulation is one of the principle of OOPs
Encapsulation is the process of hiding the internal details of an object and only exposing a public interface. 
It is achieved by using access modifiers (private, protected, public) to restrict access to the internal state of an object.
In Python, we can achieve encapsulation by using name mangling to make attributes private.
we use _ (single underscore) to indicate that an attribute is protected and __ (double underscore) to indicate that an attribute is private.
we can also use getter and setter methods to access and modify the private attributes of a class.
'''

class Employee:
    def __init__(self,salary):
        self.__salary = salary #private attribute

    def get_salary(self): #getter method to access the private attribute
        return self.__salary
    
    def set_salary(self, salary): #setter method to modify the private attribute
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary amount")
            
    
emp1 = Employee(20000)
# print(emp1.__salary)  --> this will raise an AttributeError because __salary is a private attribute
print("Salary:", emp1.get_salary()) # accessing private attribute using getter method
emp1.set_salary(25000) # modifying private attribute using setter method
print("Updated Salary:", emp1.get_salary()) 
