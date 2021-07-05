Sentence = input("Enter a word: ")

if Sentence == Sentence[::-1]: #::-1 basically just means the inverse of whatever variable it is in.
    print(f"{Sentence} is a palindrome.")    

else:
    print(f"{Sentence} is not palindrome.")


