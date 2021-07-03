# Ask a user for their personal information one question at a time. Then check that the information they entered is valid. Finally, print a summary of all the information they entered back to them.

# Example: What is your name? If the user enters * you prompt them that the input is wrong, and ask them to enter a valid name.

# # At the end you print a summary that looks like this:

# # - Name: John Doe
# # - Date of birth: Jan 1, 1954
# # - Address: 24 fifth Ave, NY
# # - Personal goals: To be the best programmer there ever was.
# -------First Example --------
fname = input("Your first name: ")
lname = input("Your last name: ")
name = fname + " " + lname
DoB = input("Your date of birth: ")
Address = input("Where do you live?: ")
Goals = input("What are your goals? \n")

print(f"Your name is: {name}")
print(f"Date of Birth is: {DoB}")
print(f"You live at: {Address}")
print(f"Your goal is: {Goals}")

# Using dictionaries
# record = int(input("Enter the student record needed to add: "))
# stud_data={}

# for i in range(0, record):
#     Name = input("Enter the student name: ").split()
#     Age = input("Enter the {} age: ").format(Name)
#     Grade = input("Enter the {} grade: ").format(Name).split()
#     Nam_key = Name[0]
#     Age_value = Age[0]
#     Grade_value = Grade[0]
#     stud_data[Nam_key] = {Age_value,Grade_value}

# print(stud_data)

# # ----this works too, sorta-----
# dictio = {
#     "Name": input("Your name: "),
#     "Age": input("Your Age: "),
#     "DoB": input("Your DoB: ")

# }

# print(dictio)

