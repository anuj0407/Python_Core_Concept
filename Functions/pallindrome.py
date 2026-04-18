# A String is a pallindrome or not
def is_pallindrome(input_string):
    #ignoring space and case sensitivity
    input_string = input_string.lower().replace(" ", "")

    # String Slicing Approach
    if(input_string == input_string[len(input_string)-1::-1]):
        return f"{input_string} is a pallindrome"
    else:
        return f"{input_string} is not a Pallindrome"

    # # Two Pointers Approach
    # left = 0
    # right = len(input_string)-1
    # while(left<right):
    #     if(input_string[left] == input_string[right]):
    #         left += 1
    #         right -= 1 
    #     else:
    #         return f"{input_string} is not a Pallindrome"
    
    # return f"{input_string} is a pallindrome"




user_input = input("Enter a String: ")
print(is_pallindrome(user_input))
