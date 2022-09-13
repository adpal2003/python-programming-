#wap to enter a number from user and print reverse of it and the number is multiply
n=int(input("enter a number:"))
s=0
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
print(s)
print(s*2)