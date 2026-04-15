#string
name = "Alice"
print(name,type(name))
# String is immutable, which means that once a string is created, it cannot be changed.

#String Functions
print(name.upper()) 
print(name.lower()) 
print(name.capitalize())
print(name.replace("Alice", "Bob")) 
print(name.split()) 
print(name[0]) 

#String slicing
print(name[0:3]) 
print(name[:3]) 
print(name[3:]) 

print(name.startswith("A"))
print(name.endswith("e")) 

