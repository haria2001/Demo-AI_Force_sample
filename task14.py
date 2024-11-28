# What is an anagram and find if the two given strings are anagrams of each other

# An anagram is a word, phrase or name formed by rearranging the letters 
# another by using all the original letters exactly once.

string1 = "listen"
string2 = "silent"

def anagram(str1, str2):
    str1 = ''.join(str1.split()).lower()
    str2 = ''.join(str2.split()).lower()
    return sorted(str1) == sorted(str2)

if anagram(string1, string2):
    print(f'"{string1}" and "{string2}" are anagram')
else:
    print(f'"{string1}" and "{string2}" are not anagram')


    
