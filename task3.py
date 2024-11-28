# Print the number of vowels in the given string

str = "Linux Os"
count = 0
for i in str:
    if i in 'AEIOUaeiou':
        count += 1
print("vowels are:", count)
