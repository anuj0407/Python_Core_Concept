'''Regex stands for Regular Expression. 
It is a sequence of characters that forms a search pattern. 
It is used to check if a string contains the specified search pattern.'''

# re module in Python provides support for regular expressions.
import re 

# check if the String contains "Python" 
txt = "Python is a programming language."
#txt = "Java is a programming language."  gives no match
# The search() function searches the string for a specified value, and returns the position of the match.
x = re.search(r"Python", txt) # r before the string indicates that it is a raw string, which means that backslashes are treated as literal characters and not as escape characters. This is important when working with regular expressions, as they often contain backslashes.
if x:
  print("Yes, there is a Python in the string!")
else:
    print("No ,there is no Python in the string!")