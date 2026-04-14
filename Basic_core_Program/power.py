N = int(input("Enter Value of N: "))
if(0<=N<31):
    for i in range(N+1):
        print(2**i)
else:
    print("Overflow")

