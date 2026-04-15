#if - else
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

#if - elif - else 
#if - else ladder
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:   
    print("Grade: B")   
elif score >= 70:
    print("Grade: C")   
elif score >= 60:
    print("Grade: D")
else:    
    print("Grade: F")


#nested if
num = 10
if num > 0:
    print("Positive number")
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Negative number or zero")