# notes from w3schools.com

# Python Data Types
x = 5
print(type(x))

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



x = b"Hello"
y = bytearray(13)
z = memoryview(bytes(13))

alist = [x, y, z] 
for a in alist:
    print(type(a))
    print(a)