def say_hello():
	print('Hello World')

say_hello()


#function_parameter

def print_max(a,b):
	if a > b:
		print(a, 'is maximum')
	elif a == b:
		print(a, 'is equal to' , b)
	else:
		print(b, 'is maximum')

print_max(3,4)

 x = 8
 y = 11	

 print_max(x,y)	

 #Local Variable

 def func(x)
 	print('x is', x)
 	x = 2
 	print('Changed local x to',x)

 x = 50
 func(x)
 print('x is still',x)

 -----------------
x = 30

def func1(x)
	x =3
def func2(x)
	x = 10

func1(x)
func2(x)
x

func1+func2

----------

#Global Statement

 def func():
 	global x

 	print('x is ',x)
 	x = 2
 	print('Change global x to', x)

 x = 50
 func()
 print('Value of x is',x)

-------------------------

 #Default Argument Values in Functions

 def say(message, times=1):
 	print(message * times)

 say('Hello')
 say('World',5)
 say('Good Bye')

 ---------------------

 def func(a, b=5, c =10):
 	print('a is',a,'and b is',b,'and c is',c)

 func(3, 8)
 func(24, c=26)
 func(c=29,a=39)

 #AvarArgs parameters
 #function_VarArgs.py
#Homework
 def total(a=5, *numbers, **phonebook)
 		print('a',a)

 		for single_item in numbers:
 			print('single_item',single_item)

 		for first_part,second_part in phonebook.items():
 			print(first_part,second_part)

 total(10,1,2,3,Jack =1123,John=2231,Inge=1459)
 
 #Return Statement

 def maximum(x,y)
 	 if x > y:
 	 	return x:	
 	 elif x == y:
 	 	return 'The numbers are equal'
 	 else:
 	 	return y

 print(maximum(3,8))
 print(maximum(20,10))

 #DocString(Documentation Strings)
		'''Prints the maximum of two numbers
		The Two values must be integers.
		'''

	x = int(x)
	y = int(y)

	if x > y :
		print(x, 'is maximum')
	else:
		print(y, 'is maximum')	

print_max(5,9)

print(print_max.__doc__)

def paper():
	'''	1.There will be situations where your 
	program has to interact with the user.
	For example, you would want to take input
	'''


print(paper.__doc__)	







