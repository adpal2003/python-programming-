#program to find the largest among three inputs.. 

num1=int(input(" enter a number1:"))
num2=int(input(" enter a number2:"))
num3=int(input(" enter a number3:"))
if num1>num2 and num2>num3:
    large=num1
elif num2>num1 and num2>num3:
    large=num2
elif num3>num1 and num3>num2:
    large=num3
print("this is largest input",large)




