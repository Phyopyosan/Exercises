#2/1/2020

# If Else Statements

>>> x = int(input("Please enter an integer:"))
Please enter an integer:5
>>> if x < 0:
...     x=0
...     print('Negative changed to zero')
... elif x==0:
...     print('Zero')
... elif x==1:
...     print('Single')
... else:
...     print('More')
... 
More

>>> x = int(input("Please enter an integer:"))
Please enter an integer:1
>>> if x < 0:
...     x=0
...     print('Negative changed to zero')
... elif x==0:
...     print('Zero')
... elif x==1:
...     print('Single')
... else:
...     print('More')
...
Single

#if else statement

>>> x = 70
>>> y = 70
>>> if x > y :
...     print("x is grater than y")
... elif x == y:
...     print("x and y are equal")
... else:
...     print("x is smaller than y")
... 
x and y are equal
>>> 

>>> x = 50
>>> y = 150
>>> if x > y:
...     print("x is grater than y")
... elif x == y:
...     print("x is equal to y")
... else:
...     print("x is less than y")
... 
x is less than y
>>>

#Short Hand If

>>> x = 80
>>> y = 70
>>> if x > y: print("x is grater than y")
... 
x is grater than y
>>> 

>>> x = int(input("Please enter exam mark:"))

Please enter exam mark:40

>>> if x < 100 & x >= 90:
...     print("A")
... elif x < 89 & x >= 70:
...     print("B")
... elif x < 69 & x >= 60:
...     print("C")
... elif x < 59 & x >= 40:
...     print("D")
... else:
...     print("Fail")
... 
Fail
>>> 


#And is logical operator

x = 50 
y = 40
z = 100
if x > y and z > x:
	   print("All conditions are True")

#Or is logical Operator

x = 40
y = 50 
z = 100
if x > y or x > y:
	 print("one of the conditions is True")
 #Nested if is if statements in if statements

 x = 50

  if x > 10:
  	print("X is ten")
  	if x > 20 :
  		print("x is grater than 20")
  	else:
  	    print ("No, x is not grater than 20")	



