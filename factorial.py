def factorial(n):
    fac =1
    for i in range(n):
        fac=fac*(i+1)
    return fac    
number=int(input("enter the number:\n"))    
print(factorial(number))    