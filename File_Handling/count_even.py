with open("File_Handling/number.txt","r") as f:
    data = f.read()
    li = data.split(",")
    even_count = 0
    for i in li:
        if(int(i)%2 == 0):
            even_count += 1
    print("Count of even numbers: ",even_count)