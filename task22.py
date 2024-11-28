# Convert the given string to a number – atoi

n = "237668"
num = 0
for char in n :
    if '0' <= char <= '9':
        num = num * 10 + (ord(char) - ord('0'))
print(num)