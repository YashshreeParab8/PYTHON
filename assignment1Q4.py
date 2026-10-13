# python class assignment
# 4. read a file, split its content into words and store them in a list- i. print total no of words
# ii. print all unique words

file = open("sample.txt", "r")

content = file.read()
words = content.split()

print("Total number of words:", len(words))

unique_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)

print("Unique words:", unique_words)

file.close()