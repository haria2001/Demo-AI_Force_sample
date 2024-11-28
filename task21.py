# Reverse each word separately in the given sentence

sentence = "I Have installed AI Force Software"
words = sentence.split()
s1 = ' '.join(word[::-1] for word in words)
print(s1)