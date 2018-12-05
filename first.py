# python by default thinks that whatever value is entered by user is a string. To change string to num,
# we can use function: int()
hours_worked = input("Please enter the hours you worked this week: ")
wage_hour = input("How much do you get per hour: ")
result = float(hours_worked) * float(wage_hour) # float print 6 tp 7 digits after decimal whereas double 16 digits
print("You will get a paycheck of $" + str(result) + " this time !")
# to print number along with string; use str() function


# tbc: python contacentaion types , or +
