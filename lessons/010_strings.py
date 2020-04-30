import os
os.system('cls')

my_string = "my name is Elodia Ka"

print ("upper: " + my_string.upper()) # CAPS
print ("lower: " + my_string.lower()) # lower case
print ("capitalize: " + my_string.capitalize()) # first letter caps, rest lower case
print ("title: " + my_string.title()) # every first letter is caps
print ("swapcase: " + my_string.swapcase()) # swaps upper & lower case

print ("len:", len(my_string)) # counts characters in string, comma-separator adds space
print ("index 0: " + my_string[0]) # prints character with index ...
print ("range 3 to 6: " + my_string[3:6]) # prints characters in  range
print ("from index 3 to end (len): " , end = '')
print (my_string[3:len(my_string)]) # prints characters from index to end
print ("split by space-character: ", end = '')
print (my_string.split(' ')[3].upper()) # split by space-character, call third index, make uppper

print ("len: ", len(my_string)) # comma adds string and int
print ("len: " + str(len(my_string))) # counts characters in string (converting int to string for print)