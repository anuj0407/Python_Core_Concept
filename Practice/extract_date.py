# using regex pattern to extract date from string

import re
data = "Today's date is 2026-04-28 and tomorrow's date will be 2026-04-29."

data_pattern = r"\d{4}-\d{2}-\d{2}"
match = re.findall(data_pattern, data)
print(match)