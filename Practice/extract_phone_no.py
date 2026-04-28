# extracting Phone Number from the data if any
import re

pattern = r"(\d{3}-\d{3}-\d{4})|(\(\d{3}\)\s\d{3}-\d{4})"
data = "Call me at 123-456-7890 or office number (987) 654-3210. Ignore 12-34-56."
matches = re.finditer(pattern,data)
for match in matches :
    print(match)
# OR
pattern1 = r"\(?\d{3}\)?[- ]?\d{3}-\d{4}"
print(re.findall(pattern1,data))