#1 Enter five Subjects marks and calculate total and percentage

M,P,C,H,E=input("Enter Five subjects marks separated by commas=").split(",")
Total = int(M)+int(P)+int(C)+int(H)+int(E)
Percentage= Total/5
print(f"Total marks={Total}")
print(f"Percentage={Percentage}")