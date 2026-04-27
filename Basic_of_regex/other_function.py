# other Regex functions include:
# compile() - Compiles a regular expression pattern into a regular expression object, which can be used for matching using its match(), search() and other methods.
import re
txt = "The rain in Spain stays mainly in the plain."
x = re.compile(r"\bS\w+") 
y = x.findall(txt)
print(y)

# split() - Splits the string at the specified pattern and returns a list.
txt = "The rain in Spain stays mainly in the plain."
x = re.split(r"\s", txt) 
print(x)
#\s matches any whitespace character (space, tab, newline, etc.).

# sub() - Replaces the matches with the text of your choice.
txt = "The rain in Spain stays mainly in the plain."
x = re.sub(r"\s", "-", txt) 
print(x)

# escape() - Escapes all the characters in a string that are not alphanumeric.
txt = "The rain in Spain stays mainly in the plain."
x = re.escape(txt)
print(x)

# subn() - Replaces the matches with the text of your choice, and returns the number of replacements made.
txt = "The rain in Spain stays mainly in the plain."
x = re.subn(r"\s", " % ", txt)
print(x)

