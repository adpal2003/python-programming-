#wap to enter a number from user and print reverse of it.

n = int(input("enter the number"))
while n > 0:
    r = n % 10
    print(r,end="")
    n = n // 10

