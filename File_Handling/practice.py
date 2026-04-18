#open a file in append mode
f = open("File_Handling/demo.txt","a")
# appending in file
f.write("\nLearned append mode in file handling")
f.close()

#or
'''
with open("File_Handling/demo.txt","a") as f:
    f.write("\nLearned append mode in file handling")
'''