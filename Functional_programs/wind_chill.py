import math
# Write a program wind_chill.py that takes two double command-line arguments t           
#and v and prints the wind chill.

#function to find wind chill
def find_wind_chill(t,v):
    return 35.74 + (0.6215*t) + ((0.4275*t - 35.75)*(math.pow(v,0.16)))

#user input for temperature(t) and wind speed(v)
t = float(input("Enter temperature(in Fahrenheit): "))
v = float(input("Enter wind speed(in miles per hour): "))

if 120<v<3 or t>50:
    print("Value are not in range to calculate the wind chill ")
else:
    print("Wind chill is: ",find_wind_chill(t,v))
