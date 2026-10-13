#python class assignment

#1.write a program to read a file and count how many vowels are present in its content
file = open("notes.txt","r");
content = file.read()
count = 0
for ch in content:
    if ch.lower() in "aeiou":
        count += 1

file.close()

print("Number of vowels:", count)