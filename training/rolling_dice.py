import random

repeat = True       # makes the start of while look possible

while repeat:       # 
    print("\n")
    print("You rolled",random.randint(1,6))
    print("Do you want to roll again? [y\\n]")
    repeat = ("y") in input().lower()