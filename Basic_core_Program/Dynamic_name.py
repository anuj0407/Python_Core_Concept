str = "Hello <<UserName>>, How are you ?"
name = input("Enter a User Name: ")
if(len(name) < 3):
    print("Name must be at least 3 characters long.")
else:
    str = str.replace("<<UserName>>", name)
    print(str)