# Ask the user to enter the full meaning of an organization or concept and you'll provide the acronym to the user. For example:

# Input -> As Soon As Possible. Output -> ASAP.
# Input -> World Health Organization. Output -> WHO.
# Input -> Absent Without Leave. Output -> AWOL.

# Example code:

# Name = [input("Please input name: ")]
# trial = list(map(lambda x: x[0], ["red", "green", "blue"]))

# ======> The four lines of code below work. Major win!!!! <======
firstname = input("Please input first name: ")
lastname = input("Please input last name: ")
name = list(map(lambda x: x[0], [firstname, lastname]))
print("Your initials are: " + ".".join(name).title()) #the title function capitalizes the first letter of each word.


# string = input("What word do you need the acronym for? Input here: ")
# word = string.split(" ")
# output = list(map(lambda x: x[0], [word]))
# print(output)
# # print( '.'.join(output))

# ====> code from the web:
text = input('Enter a string: ')
#index of first space
space1 = text.find(' ')
#index of second space
space2 = text.find(' ',space1+1)
newtext = text[0] +'. '  + text[space1+1] +'. ' + text[space2+1] +'.'
print('New string:', newtext.title())