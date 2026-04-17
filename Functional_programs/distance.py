import math

#Euclidean distance function
def euclidean_distance(x,y):
    return math.pow(math.pow(x,2)+math.pow(y,2),1/2)


x = int(input("Enter the value of X: "))
y = int(input("Enter the value of Y: "))
#calling Euclidean distance function to find distance of point(x,y) to origin(0,0)
print(euclidean_distance(x,y))


