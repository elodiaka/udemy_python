import os
os.system('cls')

my_name = "elodia"
first_names = ["john", "bob", "mary", my_name]

print(first_names[2]) #access index 2 of first_names

num = [1,2,3,4]
numbers = ['a', 'b', num]

print(numbers[2][3]) #access index 3 of index 2 (wich is a list on ints own) of numbers

first_names[0] = "Tina" #replacing entries in a list
print(first_names)

del first_names [0] #deletng  entries in a list
print(first_names)

first_names.append("Anya")
print(first_names)

print (len(first_names)) #prints number of entries
print (first_names[len(first_names) -1 ] ) #prints last entry