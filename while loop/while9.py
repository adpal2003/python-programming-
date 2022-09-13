#wap to enter a number from user and check if it is pallindrome or not
n=int(input("enter a number:"))
s=0
temp=n
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
if s==temp:
    print("this is pallindrome number:")
else:
    print("this is not pallindrome number:")
          









