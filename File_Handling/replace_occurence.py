with open("File_Handling/practice.txt","r") as f:
    data = f.read()
    new_data = data.replace("Python","Java")
    
with open("File_Handling/practice.txt","w") as f:
    f.write(new_data)