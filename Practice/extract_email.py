# extracting email from the given String
import re

pattern = r"\w+@\w+\.com" #or r"\w+@\w\.\w"
data = "Client Emails are xyz@gmail.com , abc12@go.com , pqrs@info.com "
match = re.finditer(pattern,data)
for m in match:
    print(m)