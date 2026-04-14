number = int(input("Enter a number: "))
i = 2
print("Prime factors: ",end = "")
while(i*i<=number):
    while(number%i == 0):
        print(i,end=" ")
        number=number//i
    i += 1
if(number>1):
    print(number,end =" ")
