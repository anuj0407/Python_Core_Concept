# List having top 3 winner names
player = ["Arjun" , "Hemant" , "Dhruv"]
try:
    rank = int(input("Enter a rank: "))
    print(f"{player[rank-1]} is on rank {rank}.")
except IndexError:
    print("Enter a valid rank (1,2 or 3)")
    