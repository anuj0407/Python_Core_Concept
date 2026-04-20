# Excption are errors that occur during the execution of a program. They can be handled using try-except blocks to prevent the program from crashing and to provide a way to respond to the error.

# My Inventory 
inventory = {"apple": 0.50, "banana": 0.30, "orange": 0.80}

try :
    user_item = input("Enter the item you want to buy: ")
    price = inventory[user_item]
except KeyError:
    print("Sorry, The item is not available right now.")
else:
    print(f"The price of {user_item} is ${price:}.")