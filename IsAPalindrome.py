Sentence = input("Enter a word: ")

if Sentence == Sentence[::-1]: #::-1 basically just means the inverse whatever variable it is in.
    print(f"{Sentence} is a palindrome.")    

else:
    print(f"{Sentence} is not palindrome.")
'''
        WRONG SOLUTION

# def palindrome():
#     Sentence = [input("Enter a word: ")]
#     if len(Sentence) <= 1:
#         return "This is a plalindrome"
#     if Sentence[-1] != Sentence[0]:
#         return "This is not a palindrome"

# palindrome()
'''
# def ispal(Sentence):
#     return Sentence == Sentence[::-1] 

# Sentence = input("input word: ")
# ans = ispal(Sentence)

# if ans:
#     print("Yes")
# else:
#     print("no")
