#wap to enter a number from user and print its individual digit in separte lines
n=int(input("enter a number:"))
s=0
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
while s>0:
    r=s%10
    print(r)
    s=s//10
            