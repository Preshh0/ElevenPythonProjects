# Ask the user to enter the full meaning of an organization or concept and you'll provide the acronym to the user. For example:

# Input -> As Soon As Possible. Output -> ASAP.
# Input -> World Health Organization. Output -> WHO.
# Input -> Absent Without Leave. Output -> AWOL.

string = " Hello, World! "
print(string.replace("Hello", "Hi"))
print(string.strip(" ")) #removes the stuff in the quote
# if "n" != string:
#     print("Not available")
# elif "n" in string:
#     print("AVailable!")
print(string.split("l")) #the stuff in the quotes indicates where it should cut from. NB: The whitespace is important!
# print(string1)