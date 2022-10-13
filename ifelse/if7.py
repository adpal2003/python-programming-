b=True
c=False
age=68
cost=0
if b:
    cost+=170
if c:
    cost+=50
if age<9:
    cost=int(cost*0.8)
elif age>59:
    cost=int(cost*0.7)
print("pay",cost,"rupees")    
    