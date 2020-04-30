import os
os.system('cls')

# While Loops

counter = 0
while (counter < 10):
    print("The Count is: %s" % counter) # %s inserts the variable that is called after that
    counter += 1

# For Loop

name = ["John", "Bob", "Tina"]
for x in name:                  # x is any random variable
    print (x)

fav_pizza ={
	"John": "Pepperoni",
	"Bob": "Cheese",
	"Tina": "Supreme"
}

for key, value in fav_pizza.items():    # key and value are random variables, but it has to be two of them
    print (value)