# Print the frequency of each character in the given string

n = "GenAi AI Force"
d1 = {}
for char in n:
    if char in d1:
        d1[char] += 1
    else:
        d1[char] = 1
    
print("The frequencies are: ")
for char, freq in d1.items():
    print(f"'{char}':{freq}")
