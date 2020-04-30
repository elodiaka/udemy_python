import os
os.system('cls')

# Comparison Operators
# ==
# !=
# >
# <
# <=
# >=

first_name = "John"

print ("John" == first_name) 

# If else elif

num = 10
if (num > 10):
	print ("greater than 10")
elif (num == 3):
	print("number 3")
else:
	print ("smaller than 10")

# and, or
num =3
if (num > 10) and (num < 100):		# both conditions have to be true
	print (str(num) + "is between 10 and 100")

num = 3
if (num < 10) or (num > 100):		# at least one condition has to be true (xor is more complicated)
	print (str(num) + " is not between 10 and 100")

num = 3
if (num > 10) or (num == 3):		# at least one condition has to be true (xor is more complicated)
	print (str(num) + " is greater 10 or = 3")
 