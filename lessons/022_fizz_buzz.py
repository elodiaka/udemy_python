import os
os.system('cls')

# Fizz Buzz

# print num [1:100]
# if %3==0 print Fizz
# elif %5==0 print Buzz
# elif %3==0 AND %5==0 print Fizz Buzz
# else print num

num = 0
while (num <= 100):
    num += 1
    if (num%3 == 0):
        print (str(num) + " Fizz")
#       print ("%s Fizz" % num)
    elif (num%5 == 0): 
        print (str(num) + " Buzz")
    elif (num%3 == 0 and num%5 == 0):
        print (str(num) + " Fizz Buzz")
    else:
        print (num)

    num += 1