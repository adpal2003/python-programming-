#wap to enter a number from user and print sum of its individual digit
n=int(input("enter a number:"))
tot=0
while n>0:
    b=n%10
    tot=tot+b
    n=n//10
print("the total sum of digit:",tot)















