#receiving input from user
month = input("Enter a month: ")

#finding the number of days in each month
days = 31

if month == "April" or month == "June" or month == "September" or month == "November":
    days = 30
elif month == "February":
    days = "28 or 29"

#printing result to user(concatenation)
print(month + " has " + str(days) + " days.")