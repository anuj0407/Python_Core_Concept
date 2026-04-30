'''
Question 5: Common Regex and Exception Question
Scenario:-
Create a function sanitize_input(text).
Remove unwanted special characters using re.sub().
Keep letters, numbers, spaces, and hyphens if needed.
If cleaned text becomes empty, raise InputSanitizationError.

Task:-
Write one test case for input like John Doe!.
Write one test case for input like !@#$%.
Write one test case for input like Payment: 100$.
Check cleaned output for valid text.
Check exception for empty cleaned text.
'''
import re

class InputSanitizationError(Exception):
    pass
class CleanText:
    def sanitize_input(self,text):
        clean_pattern = r'[^a-zA-Z0-9\s-]'
        clean_text = re.sub(clean_pattern, '', text)
        if not clean_text:
            raise InputSanitizationError("Empty string left after cleaning special character")
        return clean_text