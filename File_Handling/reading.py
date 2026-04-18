#opening a file to read 
f = open("File_handling/file.txt","r")
print(f.read())

#for read line by line

# to go to start of file since our file is already readded by read() and cursor is pointing at last  
f.seek(0) 
# to print all lines in file in a list form
print(f.readlines()) 

f.seek(0)
# to print a line where curson is pointing
print(f.readline())
f.close()



