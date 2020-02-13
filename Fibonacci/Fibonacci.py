# Fibonacci number module

# n = int(intput('please enter a number: '))

def fib(n): #write fibonacci series up to
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
	print()
	
# fib(200)

def fib2(n): #return Fibonacci series up to n
    result = []
    a , b =0 , 1
    while  a < n:
    	result.append(a)
    	a , b = b, a+b

    return result
