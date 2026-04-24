# Creating a Smart E-Commerce cart
from abc import ABC,abstractmethod
# for each product 
class Product:
    def __init__(self,name,price,category):
        self.name = name 
        self.price = price
        self.category = category

    def __str__(self):
        return f"Category: {self.category} | product_name: {self.name} | product_price: {self.price}"
    
# abstract class
class Discountable(ABC):
    @abstractmethod
    def apply_discount(self):
        pass

# category distribution for discount accordinly
class ElectronicProduct(Discountable):

    def apply_discount(self, original_price):#10%
        discounted_price = original_price - (original_price*(10/100))
        return discounted_price
    
class ClothingProduct(Discountable):

    def apply_discount(self, original_price):#20% if price is over 500
        if original_price > 500:
            discounted_price = original_price - (original_price*(20/100))
            return discounted_price
        else:
            return original_price
    

class GroceryProduct(Discountable):

    def apply_discount(self,original_price):
        return original_price
    
# Shopping cart main cart of user
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self,product_obj):
        self.items.append(product_obj)

    def remove_item(self,product_name):
        for item in self.items:
            if item.name.lower() == product_name.lower():
                self.items.remove(item)
                print(f"{product_name} is successfully removed !")
                return
        
    def calculate_total(self):
        # Main Logic check by type and then discount then return total bill 
        total_bill = 0
        for product in self.items:
            if product.category.lower() == "electronic":
                total_bill += ElectronicProduct.apply_discount(product,product.price)
            elif product.category.lower() == "clothing":
                total_bill += ClothingProduct.apply_discount(product,product.price)
            elif product.category.lower() == "grocery":
                total_bill += GroceryProduct.apply_discount(product,product.price)
            else:
                total_bill += product.price
        return f"Your Total bill: {total_bill}"

    def checkout(self):
        print("------ Recipt -----")
        for product in self.items:
            if product.category.lower() == "electronic":
                discounted_price = ElectronicProduct.apply_discount(product,product.price)
                print(f"Category: {product.category} | product_name: {product.name} | Original_price: {product.price} | Discounted_price = {discounted_price}")
            elif product.category.lower() == "clothing":
                discounted_price = ClothingProduct.apply_discount(product,product.price)
                print(f"Category: {product.category} | product_name: {product.name} | Original_price: {product.price} | Discounted_price = {discounted_price}")
            elif product.category.lower() == "grocery":
                discounted_price = GroceryProduct.apply_discount(product,product.price)
                print(f"Category: {product.category} | product_name: {product.name} | Original_price: {product.price} | Discounted_price = {discounted_price}")
            else:
                print(f"Category: {product.category} | product_name: {product.name} | Original_price: {product.price} ")
            
# Executing program 
# creating diffrent product
prod1 = Product("Python Programming",500,"Book")
prod2 = Product("Fan",1299,"Electronic")
prod3 = Product("Over-sized T-shirts",399,"Clothing")
prod4 = Product("Dinner-set",899,"Grocery")

print("----- Welcome to E-Commerce Cart -----\n")
cart = ShoppingCart()
cart.add_item(prod1)
cart.add_item(prod2)
cart.add_item(prod3)
cart.add_item(prod4)

cart.checkout()
print()
print(cart.calculate_total())

cart.remove_item("Dinner-set")
print()
print(cart.calculate_total())