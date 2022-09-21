#wap to enter a 5 value from user and append them into a list and print sum of the list without using sum function
i=1
temp=0
l=[]
while i<=5:
    n=int(input("enter a value:"))
    temp=temp+n
    l.append(n)
    i+=1
print(l)
print(temp)