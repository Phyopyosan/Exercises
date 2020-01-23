Loops.py

-While Loops
-for Loops

Condition is true, while loop execute a set of statements

x = 1
 while x < 7:
 	print(x)
 	x +=1

while loop requier variable ready

x = 1
 while x < 7 :
 	    print(x)
 	    if x == 5 :
 	    	break
 	    x += 1

For Loops
	
#for loops is iterating over a sequence

fruits = ["apple", " banana" , "orange" , "pineapple" , "cocount", "cucumber"]
for x in fruits:
	print(x)

#Looping in a String 

for x in "pineapple":
	print(x)

#the break statement
fruits = ["apple", " banana" , "orange" , "pineapple" , "cocount", "cucumber"]
for x in fruits:
	print(x)
	if x == "pineapple"
		break

for x in fruits:
	if x == "pineapple"
		break	
		print(x)	
		

#The continue statement - Stop the current iteration

for x in fruits:
	if x == "pineapple":
		continue
	print(x)

for x in fruits:
	if x == "pineapple" or x == "cocount":
		continue
	print(x)


#The range() function - a set of a code a specified number of items

for x in range(10):
     print(x)


for x in range(10,100)
	print(x)  

for x in range(10,100,5): # 5 is jump
	print(x)


#Nested Loops	

NumberA = [1 , 2, 3, 4, 5]
NumberB = [1 , 2, 3, 4, 5]

for x in NumberA:
		for y in NumberB:
			print(x,y)

for x in NumberA:
		for y in NumberB:
			for z in [1,2,3,4,5]:
			      print(x,y)
#pass 

   for x in [1,2,3,4,5]:
   		pass

......

 words = ['cat' , 'window' , 'defenstrate']
 for w in words:
 	print(w, len(w))   

 ......

 for n in range(2, 10):
 	for x in range(2, n):
 		if n % x == 0:
 			print(n, 'equals', x, '*', n//x)
 			break
 	else:
 		#loop fell through winthout finding a factor
 		print(n, 'is a prime number')	

.......

for num in range(2,10):
	if num%2 == 0:
		print("Found an even number" , num)
		continue
	print("Found a number",num)	

for num in range(2,10):
	if num%2 == 0:
		print("Found an even number" , num)
		break
	print("Found a number",num)	

for num in range(2,10):
	if num%2 == 0:
		print("Found an even number" , num)

	print("Found a number",num)		







 		


