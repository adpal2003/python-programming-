#5 Write a python program to find power of any number x ^ y. by importing math module using pow() function. 
import math
base,exp=input("enter a base and exponant by seperated commas:=").split(",")
power=math.pow(int(base), int(exp))
print(f"the power {base}^{exp} = {power}")












