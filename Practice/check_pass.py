# condition for password :- contains at least one digit or at least one uppercase letter
import re

password = input("Enter your password:-")

pass_pattern = r"[0-9A-Z]"
match = re.findall(pass_pattern, password)
if match:
    print("Password created successfully!")
else:
    print("Enter a valid password which must contain one Uppercase letter or one digit.")