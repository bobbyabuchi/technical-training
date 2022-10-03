# notes from w3schools.com

# ..........................................................................Python Data Types

x = 5
print(type(x))

# a dictionary of some data types in Pyhton
python_data_types = {
    "str": 'x = "Hello Bob"', 
    "int":'x = 2022',
    "float":'x = 09.29',
    "complex":'5j',
    "list":'["cars", "computers", "phones"]',
    "tuple":'("notes", "pen", "texts")',
    "range":'range(8)',
    "dict":'{"name": "Bobby", "age": 32}',
    "set":'{"bananas", "twining", "berries"}',
    "frozenset":'({"bananas", "twining", "berries"})',
    "bool":'True',
    "bytes":'b"Word"',
    "bytearray":'bytearray(5)',
    "memoryview":'memoryview(bytes(5))',
    "NoneType":'None'
}

# one can acutally set a specific data type, especially if you left C/C++ but they haven't left you
# just invoke the data type as a method
x = str("Hello World")
x = int(20)
x = float(20.22)

# ..........................................................................Python Numbers

# three numeric types (int, float and complex) in Python
a = 13
b = 20.22
c = 1j
d = 12E4    # float
e = 10e22   # still float


# verify type of an object
print(type(a),type(b),type(c),type(d),type(e))

# random numner
import random
print(random.randrange(1, 10)) # display a random number from 1 - 9, excluding 10 

# ..........................................................................Python Casting
# this is the same as specify a variable type
# done with constructor functions int(), float(), str()

# convert float to int
a = 22.20
print(int(a)) # prints 22

# ..........................................................................Python Strings

# multiline strings with double or single qoute
a = """
This is a multiline string
will read and interpret the white spaces and 
line breaks
"""
print(a)

# arrayish nature of strings
a = "Hello, Word!"
print(a[0])

# loop through a string
a = "BobbyAbuchi"
for b in a:
    print(b)
print(len(a))

# scan a text for a bunch of characters
c = "The lines are fallen unto me in pleasant places! I have a godly heritage."
print("godly" in c)

if "godly" in c:
    print("Yes, he said godly.")

if "agwa" not in c:
    print("No mention of agwa here.") 

# slicing strings - this counts commas and white spaces
a = "ABCDE,EFGH IJKL"
print(a[2:6])

# slice from start
print(a[:5])

# slice to end
print(a[3:])

# negative indexing
print(a[-6:-2])

# 

# ..........................................................................Python Booleans



# ..........................................................................Python Operators
# ..........................................................................Python Lists
# ..........................................................................Python Tuples
# ..........................................................................Python Sets
# ..........................................................................Python Dictionaries
# ..........................................................................Python If...Else
# ..........................................................................Python While Loops
# ..........................................................................Python For Loops
# ..........................................................................Python Functions
# ..........................................................................Python Lambda
# ..........................................................................Python Arrays
# ..........................................................................Python Classes/Objects
# ..........................................................................Python Inheritance
# ..........................................................................Python Iterators
# ..........................................................................Python Scope
# ..........................................................................Python Modules
# ..........................................................................Python Dates
# ..........................................................................Python Math
# ..........................................................................Python JSON
# ..........................................................................Python RegEx
# ..........................................................................Python PIP
# ..........................................................................Python Try...Except
# ..........................................................................Python User Input
# ..........................................................................Python String Formatting