# Data cleaning
import re

text = "  This   is   a sentence   with    Extra spaces.   "
text = text.strip()
pattern = r"\s+"
cleaned_text = re.sub(pattern," ",text)
print(cleaned_text)
