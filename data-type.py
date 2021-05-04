#Variable
counter = 100
miles = 1000.0
name = "John"

print (counter)
print (miles)
print (name)

#Multiples assigment
a=b=c=1
#Python allows you to assign a single value to several variables.
print(a, b, c)

d,e,f= "Liam","Marvin","Jaz"
#Multiple Assignment
print(d,e,f)


#Python Numbers
var1 = 1
var2 = 2
print(var1, var2)
del var2


#Python String
str = 'Hello World!'
print (str)
print (str[0])
print (str[2:5])
print (str[2:])
print (str * 2)
print (str + "TEST")

#Python List
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)
print (list[0])
print (list[1:3])
print (list[2:])

print (tinylist * 2)
print (list + tinylist)

#Python Tuple
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')

print (tuple)
print (tuple[0])
print (tuple[1:3])
print (tuple[2:])

print (tinytuple * 2)
print (tuple + tinytuple)

'''
The following code is invalid with tuple, 
because we attempted to update a tuple, which is not allowed

tuple[2] = 1000
list[2] = 1000
print (tuple)

'''

#Python Dictionary
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print (dict['one'])
print (dict[2])
print (tinydict)
print (tinydict.keys())
print (tinydict.values())

'''
Data Type Conversion
Sometimes, you may need to perform conversions between the built-in types. To convert between types, you simply use the type-name as a function.

There are several built-in functions to perform conversion from one data type to another. These functions return a new object representing the converted value.

int(x [,base]): Converts x to an integer. The base specifies the base if x is a string.
float(x): Converts x to a floating-point number.
complex(real [,imag]) : Creates a complex number.
str(x) : Converts object x to a string representation.
repr(x) : Converts object x to an expression string.
eval(str) Evaluates a string and returns an object.
tuple(s) : Converts s to a tuple.
list(s) : Converts s to a list.
set(s) : Converts s to a set.
dict(d) : Creates a dictionary. d must be a sequence of (key,value) tuples.
frozenset(s) : Converts s to a frozen set.
chr(x) : Converts an integer to a character.
unichr(x) : Converts an integer to a Unicode character.
ord(x) : Converts a single character to its integer value.
hex(x) : Converts an integer to a hexadecimal string.
oct(x) : Converts an integer to an octal string.
'''