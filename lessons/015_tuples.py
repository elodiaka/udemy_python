import os
os.system('cls')

tuple_1 = ('John', 'Bob', 'Mary')

print(tuple_1[0])

tuple_2 = ("Sina", ) # tuple with single entry get a coma at the end, otherwise it's a string
tuple_3 = tuple_1 + tuple_2

print(tuple_3)

tuple_4 = tuple_1[0:2] # range: from 0 up until but not including 2

print(tuple_4)

tuple_5 = tuple_1[0:2] + tuple_2 # adding tuples
print(tuple_5) 