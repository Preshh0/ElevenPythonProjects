# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# name = input('Enter your name: ')
# age = input('Enter your age: ')
# p1 = Person(name, age)
# print("Your name is: ", p1.name)
# print("Your age is: ", p1.age)

# def get_max(list):
#     return max(list, key = len)

# array = ["Boy", "Gir", "Can"]
# print(get_max(array))

# class Solution(object):
def two_sums( num, target):
    num_to_index = {}

    for i, num in enumerate(num):
        if target - num in num_to_index:
            return [num_to_index[target - num], i]
        num_to_index[num]= i
    return []

num = [1,2,4]
target = int(input("Input target number: "))
print(two_sums(num, target))

gigi = [5,6,7,8]
print(list(enumerate(gigi)))
for number in gigi:
    print(gigi)

hio = 123
print(hio)
do = [1,2,34.6,7,8]
do.sort()
do.reverse()
print(do)

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
# # # name.split()
# # ouput = slice([1], [2])
# # print(name[ouput])
# for letter in name:
#     print(letter[(0)])

def get_max_str(lst):
    return max(lst, key=len)

name = ["hi", "hwlo","hello", "boy"]
print(get_max_str(name))

# nae = 1234
# print(ascii("a"))
print(callable(29))