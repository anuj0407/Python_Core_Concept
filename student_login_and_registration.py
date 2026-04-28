# Student Login and Registration Regex Practice Problem
'''
Create a Python program for a student registration and login system using regular expressions
Registration rules:--
-Student name: Must contain only letters and spaces, and length should be 3 to 30 characters.
-Address: Must contain letters, numbers, spaces, commas, periods, hyphens, and slashes, and length should be 10 to 100 characters.
-Student ID: Must start with STU followed by exactly 4 digits, for example STU1024.
-Password: Must be 8 to 16 characters long and contain at least one uppercase letter, one lowercase letter, one digit, one special character, and no spaces.
'''
import os
import json
import re

def registration():
    while True:
        print("------ Welcome to Registartion page ------\n")
        name_pattern = r'[A-Za-z\s]{3,30}'
        address_pattern = r'[A-Za-z0-9\s\,\\-]{10,100}'
        id_pattern = r'^(STU)\d{4}'
        password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%^&*])(?!.*\s).{8,16}$"

        print("Note:- Fill the correct details.\n")
        student_name = input("Enter your name: ")
        if not re.match(name_pattern,student_name):
            print("Error: Student name is not as per the guidelines.")
            continue
        
        student_address = input("Enter your address: ")
        if not re.match(address_pattern,student_address):
            print("Error: Student address is not as per the guidelines.")
            continue

        student_id = input("Enter your ID: ")
        if not re.match(id_pattern,student_id):
            print("Error: Student ID is not as per the guidelines.")
            continue

        student_password = input("Enter your password: ")
        if not re.match(password_pattern,student_password):
            print("Error: Student password is not as per the guidelines.")
            continue

        new_entry = {
                "ID":student_id,
                "Password":student_password,
                "Name":student_name,
                "Address":student_address
                }
        
        file_path = "Student_Data.json"
        if os.path.exists(file_path):
            with open(file_path,"r") as f:
                data = json.load(f)
        else :
            data = []
        data.append(new_entry)
        with open(file_path,"w") as f:
            json.dump(data,f,indent=2)

        print("Registration Successful")
        break


def login():
    print("------ Weloome to Login page ------\n")
    student_id = input("Enter your Id: ")
    student_password = input("Enter your password: ")

    file_path = "Student_Data.json"

    if os.path.exists(file_path):
        with open(file_path,"r") as f:
            data = json.load(f)
    else :
        print("There is no student data, First register yourself!")
    
    found = False
    for info in data:
        if info["ID"] == student_id and info["Password"] == student_password:
            print("Login successful")
            found = True
            break
    
    if not found:
            print("Invalid student ID or password")
        

# Execution of Program
print("------ Welcome to Neo_AI ------\n")
while True:
    print("1. Enter 1 to register yourself\n2. Enter 2 for Login\n3. Enter 3 to exit..")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        registration()
    elif choice == 2:
        login()
    elif choice == 3:
        print("Terminating the program.")
        break
    else:
        print("Invalid choice , Select the right choice.")
