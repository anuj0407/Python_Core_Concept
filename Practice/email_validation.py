# Email validation 
'''
Rules:-
1. Username can contain alphabets(uppercase,lowercase,_,.)
2. Username can contain digits but can't start with digit
3. Format should be username@domain.com
4. Domain must contain alphabets(uppercase,lowercase)
'''

import re

email = input("Enter your Email: ")
pattern = r"^[A-Za-z_][\w+_]+@[A-Za-z]+\.com$"

match = re.match(pattern,email)
if match:
    print("Valid Email")
else :
    print("Invalid Email")