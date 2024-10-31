#User Input Data Processor
#Objective: The aim of this assignment is to process and format user input data

#Task 1: Input Length Validator Write a script that asks for and checks the length of the user's first name and last name. \\n
# Both should be at least 2 characters long. If not, print an error message.


def user_input():
    first_name = input("Enter your first name. ")
    if len(first_name) <2:
        print("First name must be at least 2 character long.")
    return {first_name}
    last_name = input("Enter your last name. ")
    if len(last_name) <2:
        print("Last name must be at least 2 characters long.")

user_input()    