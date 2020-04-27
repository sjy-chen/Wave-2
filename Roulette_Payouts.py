#importing random module
import random

#generating the value of a random space 
space_value = random.randint(0,37)

#representing 00 using 37
if space_value == 37:
    print("The spin resulted in 00...")

#printing all other numbers
else:
    print("The spin resulted in {}...".format(space_value))

#finding the payout value
if space_value == 37:
    print("Pay 00")
else:
    print("Pay", space_value)

#finding colour(not done for 0 and 00)
if space_value != 37 and space_value !=0:
    if space_value == 1 or space_value == 3 or space_value == 5 or space_value == 7 or space_value == 9\
    or space_value == 12 or space_value == 14 or space_value == 16 or space_value == 18 \
    or space_value == 19 or space_value == 21 or space_value == 23 or space_value == 25 or space_value == 27\
    or space_value == 30 or space_value == 32 or space_value == 34 or space_value == 36:
        print("Pay Red")
    else:
        print("Pay Black")

#finding if even or odd(not done for 0 and 00)
if space_value != 37 and space_value !=0:
    if space_value % 2 == 0:
        print("Pay Even")
    else: 
        print("Pay Odd")

#finding lower or upper 
if space_value != 37 and space_value !=0:
    if space_value >= 1 and space_value <= 18:
        print("Pay 1 to 18")
    else:
        print("Pay 19 to 36")