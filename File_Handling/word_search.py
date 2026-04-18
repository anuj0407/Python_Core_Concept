word = "learning"
with open("File_Handling/practice.txt","r") as f:
    data = f.read()
    
    if(data.find(word) != -1):
        print("Found!")
    else:
        print("Not Found!")