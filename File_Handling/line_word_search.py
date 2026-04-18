
def check(word):
    data = True
    line = 1
    with open("File_Handling/practice.txt","r") as f:
        while(data):
            data = f.readline()
            if(word in data):
                return line
            line += 1
    return -1

word = "Java"
line_no = check(word)
if(line_no != -1):
    print(f"Found! in line {line_no}")
else:
    print("-1")