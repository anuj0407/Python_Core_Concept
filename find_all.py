# findall() in regex is a function that returns a list of all matches of a pattern in a string. 
# It is used to find all occurrences of a pattern in a string and return them as a list.

import re
txt = "The rain in Spain stays mainly in the plain."
x = re.findall(r"\w+in\b", txt) # The findall() function returns a list containing all matches of the pattern in the string.
print(x) 

#\w matches any alphanumeric character (letters and digits) and the underscore character.
#\b is a word boundary, which means that the pattern will only match if it is at the end of a word.