#wap to enter a number from user print its individual digits in character from
n=int(input("enter a number: "))
s=0
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
while s>0:
    r=s%10
    if r==1:
        print("one")
    elif r==2:
        print("two")
    elif r==3:
        print("three")
    elif r==4:
        print("four")
    elif r==5:
        print("five")
    elif r==6:
        print("six")
    elif r==7:
        print("seven")
    else:
        print("zero")
        
    s=s//10
    
        
    