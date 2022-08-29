var=int(input("how many row you want to print:"))
print("type 1 or 0")
var1=int(input())
new=bool(var1)
if new == True:
    for i in range(1,var+1):
        for j in range(i,i+1):
            print("*",end=" ")
        print()
elif new == false:
    for i in range(i,var-1):
        for j in range(i,i-1):
            print("*",end=" ")
        print()    







