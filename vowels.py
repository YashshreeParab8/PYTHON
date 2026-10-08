#accept sentence from user and count the vowels
# s=input("Enter a sentence:")
# count=0
# for i in s:
#     if i in "aAeEiIoOuU":
#         count+=1
# print("total vowels are:",count)

#passing count of vowels
s=input("Enter a string:")
vowels="aAeEiIoOuU"
hm={}
for i in s:
    if i in vowels:
        hm[i]=hm.get(i,0)+1

for i in hm:
    print(i,":",hm[i])