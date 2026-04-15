number = int(input("Enter a number: "))
if number < 0:
    print("The number is negative. Please enter a non-negative number.")
else:
    for i in range(1,11):
        print(f"{number} x {i} = {number * i}")
