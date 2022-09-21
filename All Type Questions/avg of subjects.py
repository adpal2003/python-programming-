sub1=int(input("enter the markes first subject: "))
sub2=int(input("enter the markes second subject: "))
sub3=int(input("enter the markes third subject: "))
avg=(sub1+sub2+sub3)/3
print(avg)
if avg>90:
    print("Grade A")
elif avg>=80 and avg<=90:
    print("Grade B")
elif avg>=70 and avg<=80:
    print("Grade C")
elif avg>=60 and avg<=70:
    print("Grade D")
else:
    print("Grade F")























