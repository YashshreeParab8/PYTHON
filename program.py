# #8/10/26
# #string functions
# text = "  Hi! I'm Yashashree  "
# print("Original text:",text)

# #strip function
# print("Strip function:",text.strip())

# #count function
# print("Count of letter a:",text.count('a'))

# #find function
# print("Position of Y:",text.find('Y'))

# #replace()
# print("Replaced text:", text.replace('Yashashree','Ananya'))

# #startswith()
# print(text.startswith('A'))

# x = int(input("Enter a number:"))
# if x>0:
#     print("Number is positive")
# elif x==0:
#     print("Number is zero")
# else:
#     print("Number is negative")

# count = 0
# while count<5:
#     print(count)
#     count+=1

# for i in range(5):
#     print(i)

name = 'Yashashree'
vowels= 'aAeEiIoOuU'
for i in name:
    if vowels in name:
        print(name.replace(vowels,'z'))