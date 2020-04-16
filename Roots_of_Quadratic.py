#importing math
import math

#asking for inputs from user:
a = input("Enter the a value: ")
b = input("Enter the b value: ")
c = input("Enter the c value: ")

#turning the values into floats
a = float(a)
b = float(b)
c = float(c)

#finding the discriminant
discriminant = b**2 - 4*a*c

#discriminant is negative
if discriminant < 0:
    print("There are no real roots.")

#discriminant is 0
elif discriminant == 0:
    print("There is one real root.")

    root = ((-1)*b) / (2*a)

    print("The real root is " + str(root) + ".")

#discriminant is positive
elif discriminant > 0:
    print("There are two real roots.")
    
    squared_discriminant = math.sqrt(discriminant)

    root_1 = ((-1)*b+squared_discriminant) / (2*a) 
    root_2 = ((-1)*b-squared_discriminant) / (2*a)  
       
    print("The real roots are " + str(root_1) + " and " + str(root_2) + ".")