n = int(input("Enter how many number in an array: "))
li = []
for i in range(0,n):
    value = int(input("Enter no. : "))
    li.append(value)

no_of_triplet = 0
triplet = []
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if(li[i]+li[j]+li[k] == 0):
                no_of_triplet += 1
                triplet.append([li[i],li[j],li[k]])
                

print(f"No. of triplet that sum to exactly 0 is {no_of_triplet}")
print("triplets are:--")

print(triplet)


