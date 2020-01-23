x = int(input("Examination Result:"))

if x <= 100 and x >= 90 :
	print("Grade A")
elif x < 90 and x >= 70:
	print("Grade B")
elif x < 70 and x >=60 :
	print("Grade C")
elif x < 60 and x >= 40:
	print("Grade D")
elif x < 40 and x >= 10:
	print("Fail")
else: 
	print("Nothing wrong")					
