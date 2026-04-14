N = int(input("Enter Harmonic value N:"))
if(N == 0):
    print("Invalid input!!")
else:
    sum = 0
    for i in range(1,N+1):
        sum += (1/i)
    print(sum)