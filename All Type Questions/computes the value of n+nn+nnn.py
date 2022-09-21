#Write a Python program that accepts an integer (n) and
#computes the value of n+nn+nnn.
#Sample value of n is 5
#Expected Result : 615

n=int(input("Enter a number:"))
temp=str(n)
temp1=temp+temp
temp2=temp+temp+temp
cal=n+int(temp1)+int(temp2)
print(cal)









