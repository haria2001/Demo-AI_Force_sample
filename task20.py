# Find the frequency of the words in the given sentence

sentence = "I Have installed AI Force Software"
sentence= sentence.lower()
words = sentence.split()
d1 ={}
for word in words:
    if word in d1:
        d1[word] += 1
    else:
        d1[word] = 1
for word, count in d1.items():
    print(f"{word}:{count}")
