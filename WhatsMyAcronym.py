# Ask the user to enter the full meaning of an organization or concept and you'll provide the acronym to the user. For example:

# Input -> As Soon As Possible. Output -> ASAP.
# Input -> World Health Organization. Output -> WHO.
# Input -> Absent Without Leave. Output -> AWOL.

# string = " Hello, World! "
# print(string.replace("Hello", "Hi"))
# print(string.strip(" ")) #removes the stuff in the quote
# # if "n" != string:
# #     print("Not available")
# # elif "n" in string:
# #     print("AVailable!")
# print(string.split("l")) #the stuff in the quotes indicates where it should cut from. NB: The whitespace is important!
# # print(string1)\

# name = "Hello World"
# name.split(" ")
# for i in name:
#     for j in name:
#         print(name[1])
#     print(name[0])

value = input("Input a value: ")
 

if type(value) == str:
    print("It is a string.")
if type(value) == int:
    if value is range (0,99):
        print("It is an integer.")
if type(value) == bool:
    print("It is a boolean.")
if type(value) == list:
    print("It is a list.")