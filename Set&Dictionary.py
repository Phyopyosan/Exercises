#Sets

Sets = {}
																																														
#includes a data types for sets
#Curly braces or the set() function can be used to create sets.

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
#show duplicated data have been removed


#Demostrate Set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a 								#unique letterss in a
a - b 							#letters in a but not in b
a | b 							#letters in a or b or both
a & b 							#letters in both a and b
a ^ b 							#letters in a or b but not b

a = {x for x in 'abracadabra' if x not in 'abc'}
a

a = {x for x in 'abracadabra' if x  in 'abc'}
a

if x in 'abc'
	for x in 'abracadabra'

print(x)


fruits = {"apple" , "banana", "cherry", "orange", "kiwi", "melon", "mango"}
print("cherry" in fruits)		

fruits.add("cucumber")
fruits

fruits.update("grape")
fruits

fruits.remove("banana")
fruits

fruits.discard("kiwi")
fruits

>>>Dictionaries 

#Dictionaries

#Another useful data type built into Python is the dictionary

tel = {'jack': 4098, 'sape' : 4139}
tel['jack']
tel['guido'] = 4127
del tel['sape']

list(tel)

sorted(tel)

'guido' in tel
'sape' not in tel

dict([('sape',4139),('guido', 4127), ('jack', 4098)])
dict(sape = 4139 , guido = 4127, jack= 4098)
dict(4139 , 4127, 4098)

{x: x**2 for x in (2, 4, )}
{x: x**3 for x in (1, 2, 3, 4, 5)}

#When looping through dictionareis

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
	print(k, v)



