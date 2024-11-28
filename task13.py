# What is a pangram and find if the given sentence is a pangram

# A pangram is a sentence or phrase that contains all the letters of the alphabet at least once.
sentence = input("Enter a sentence: ")
sentence = sentence.lower()
albhabet = 'abcdefghijklmnopqrstuvwxyz'

is_panagram = True
for letter in albhabet:
    if letter not in sentence:
        is_panagram = False
if is_panagram:
    print("the sentence is pangram")
else:
    print('the sentence is not pangram')