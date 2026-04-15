m = int(input("Enter no. of rows: "))
n = int(input("Enter no. of coloumn: "))
array = []
for i in range(m):
    li = []
    for j in range(n):
        value = int(input("Enter a value: "))
        li.append(value)
    array.append(li)

for i in range(m):
    for j in range(n):
        print(array[i][j],end = " ")
    print()