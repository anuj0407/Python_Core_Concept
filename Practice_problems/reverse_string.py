string_1 = input("Enter a string: ")
reverse_string = ""
for i in range(len(string_1)-1, -1,-1):
    reverse_string += string_1[i]
print(f"Reverse of String: {string_1} is: {reverse_string}")