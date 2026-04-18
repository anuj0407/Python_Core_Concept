#opening a file to write 
f = open("File_Handling/abc.txt","w")

# if a file is present then the write function override the content written in file and if there is no such file it creates a file and write in that
# f.write("Hello world! Learning file handling")

#copying file.txt content to abc.txt
f1 = open("File_Handling/file.txt","r")

for data in f1:
    f.write(data)