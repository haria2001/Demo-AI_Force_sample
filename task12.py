# What is a palindrome and find if the given number is a palindrome number

# A palindrome is a word, phrase, number or any sequence of characters that reads same backward as forward.
n = 121
if str(n) == str(n)[::-1]: 
    print ("palindrome")
else:
    print("not palindrome")
    
