#receiving number from user
number = input("Enter an integer: ")

#converting input to int
number = int(number)

#determing if integer is even or odd 
if number % 2 == 0:
    print(str(number) + " is even.")
else: 
    print(str(number) + " is odd.")