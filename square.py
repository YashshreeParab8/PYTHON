#accept 2 values s and n. print squares of first n number starting from s
s=int(input("Enter starting digit:"))
n=int(input("enter range:"))
for i in range(s,s+n):
    print(i*i)