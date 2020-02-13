#Boolean Expression

print(20 > 10)
print(20 == 10)
print(20 < 10)
print(bool("Hello World"))
print(bool(20))


Python Condition

Equals 								-> x == y
Not Equals							-> x != y
Less Than							-> x <  y
Less Than or Equals to 				-> x <= y
Greater than 						-> x >  y
Grater than or equal to 			-> x >= y
Boolean OR 							-> x or y , x | y
Boolean AND     					-> x and y , x & y
Boolean NOT 						-> not x


#if statement
  
  x = 70
  y = 60


  if x > y:
  	print("x is grater than y")

  if x < y:
   	print(" x is not grater than y")

  elif x == y:
  	print("x is equal to y") 

  elif x > y:
  	print("x is grater than y")		

  elif x != y:
  	print("x is not equal to y")

  elif y < x:
  	print("y is smaller than x")			

  else:
  	print("x is grater than y") 


 #short hand if
 
 if x > y: print("x is grater than y") 	


 x= 50
 y = 150

if x > y: print("x is grater than y") 
elif x ==y : print("x is equal to y") 
else: print("xis less than y")	


print(x) if x > y else print(y)

#And is logical operator

x = 50
y = 40
z = 100
if x > y and z > x:
	print("All Condition are True")


#Or logical operator

x = 50
y = 40
x = 100

if x > y or z > y: 
	print("one of the Condition is true")
elif x > y and z > y:
	print ("All Condition are true")
else:
	print("nothing else")		

if x > y and z < y or x < y:
	print("Line No1 is True")
elif x < x or y < x or z == y:
	print("Line No2 is true")
elif z > y and x > y and x!= y :
	print("Line No 3 is true")
else:
	print("Nothing else")


#Nested If is  if statement in if statement

	x = 50

	if x > 10:
	   print("x is ten")
	   if x > 20:
	     	print("x is grater than 20")
	   else: 
	        print("No, x is not grater than 20")
	elif x < 10:
	   print("x is small")
	   if x < 5:
	   	  print("x is small than 5")
	   	else:
	   		print("No, x is nothing")
	else:
		print("x is biggest")   

  
  #Pass Statement

   x = 100
   y = 50

   if x > y :
   		Pass

   if x > y :
   		print("x is grater than 10 and 20")
   		pass		
   		print("x is not grater than 10 & 20 ")				        				



