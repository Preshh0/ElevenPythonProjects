Sentence = [input("Enter a word: ")]
res = [i[:: -1] for i in Sentence]

if Sentence == res:
    print(f"{Sentence} is a palindrome.")    

else:
    print(f"{Sentence} is a palindrome.")