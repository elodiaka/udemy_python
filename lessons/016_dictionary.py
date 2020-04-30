import os
os.system('cls')

# Dictionaries also calles hashes in other programming languages

fav_pizza ={
	"John": "Pepperoni",
	"Bob": "Cheese",
	"Tina": "Supreme"
}
print (fav_pizza['John'])                   # call by value prints the key

del fav_pizza['John']
print (fav_pizza) 

fav_pizza["Jake"] = "Ham"                   # adding key and value to end of dict
fav_pizza.update({"Tim": "Green Peppers"})  # adding key and value to end of dict
print (fav_pizza) 

fav_pizza.update({"Tim": "Red Peppers"})    # updating value of the called key
fav_pizza["Jake"] = "Hawaii"                # updating value of the called key
print (fav_pizza) 

fav_books = { 42: "Answer" 
}               # updating value of the called key
print (fav_books) 