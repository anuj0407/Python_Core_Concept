string_1 = input("Enter a string: ")
counter = 0
for i in range(0, len(string_1)):
    if(string_1[i] == 'a' or string_1[i] == 'e' or string_1[i] == 'i' or string_1[i] == 'o' or string_1[i] == 'u'):
        counter += 1

print(f"The given string contains {counter} number of Vowels.")
