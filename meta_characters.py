# Meta Characters in regex are special characters that have a specific meaning and are used to define patterns in regular expressions.
# Some common meta characters include:
# .  - Matches any character except a newline.
# ^  - Matches the start of a string.    
# $  - Matches the end of a string.
# *  - Matches zero or more occurrences of the preceding character or group.
# +  - Matches one or more occurrences of the preceding character or group.
# ?  - Matches zero or one occurrence of the preceding character or group.
# [] - Matches any single character within the brackets.
# |  - Acts as a logical OR between patterns.
# () - Groups patterns together and captures the matched text.
# \  - Escapes a special character, allowing it to be treated as a literal character.
# {} - Specifies a specific number of occurrences of the preceding character or group.

import email
import re
data = "mail abc@def.com, mail xyz@uvw.com"
# To find all email addresses 
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
matches = re.findall(pattern, data)
print(matches)

data1 = {
    "name" : "Arjun",
    "email" : "arjun@gmail.com"
}
pattern1 = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
matches1 = re.findall(pattern1, data1["email"]) 
print(matches1)