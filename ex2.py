# Problem 1- Create a program that displays your name and complete mailing address. The address should be printed in the format
#that is normally used in the area where you live. Your program does not need to read any input from the user.
print("Bunyamin Fuat Yildiz")
print("Department of Economics")
print("University of Rutgers")
print("Clifton, NJ")
print("United States of America")









# Problem 3: Write a program that asks the user to enter the width and length of a room. Once these values have been read, your program should
#compute and display the area of the room. The length and the width will be entered as ﬂoating-point numbers.
#Include units in your prompt and output message; either feet or meters, depending on which unit you are more comfortable working with.
length = input(float("Enter the length of the room")
width = input(float("Enter the width of the room")
area = lengt * width
print("the area of your room is", area, square feet)


# Problem 4: Create a program that reads the length and width of a farmer’s ﬁeld from the user in
# feet. Display the area of the ﬁeld in acres. Hint: There are 43,560 square feet in an acre.

SQFT_PER_ACRE = 43560

length = input(int("Enter the length of the field in feet :"))         
width = input(int("Enter the width of the field in feet:"))
acres = length * width / SQFT_PER_ACRE
    
print(" The area of the field is," acres, "acres")

# PROBLEM 5: Inmany jurisdictions a small deposit is added to drink containers to encourage people  to recycle them. In one particular jurisdiction,
#  drink containers holding one liter or less have a $0.10 deposit, and drink containers holding more than one liter have a $0.25 deposit.
# Write a program that reads the number of containers of each size from the user. Your program should continue by computing and displaying the refund that will be
# received for returning those containers. Format the output so that it includes a dollar sign and two digits to the right of the decimal point


less_deposit = 0.10
more_deposit = 0.25


less = input(int("How many containers 1 liter or less?")
more = input(int("How many containers more than 1 litre?"))

refund = less* less_deposit + more * more_deposit

print("Your total refund will be $%.2f." %refund) #note the %2f format specifier indicates that a value should be formatted as a floatin-point number with 2 digits to the right of the decimal point.

# Problem 6: The program that you create for this exercise will begin by reading the cost of a meal ordered at a restaurant from the user. Then your program will compute the tax and
# tip for the meal. Use your local tax rate when computing the amount of tax owing. Compute the tip as 18 percent of the meal amount (without the tax). The output from
# your program should include the tax amount, the tip amount, and the grand total for the meal including both the tax and the tip. Format the output so that all of the values
# are displayed using two decimal places.

tax_rate = 0.05
tip_rate = 0.18

cost = float(input("Enter the cost of the meal:"))
             
  tax = cost * Tax_rate
  tip = cost * tip_rate
  total= cost+ tax+ tip

print( " The tax is %.2f and the tip is %.2f, making the",
       \"total %.2f" % (tax, tip, total)) "








# Problem 10 : Create a programthat reads two integers, a and b, fromthe user.Your programshould compute and display:
#• The sum of a and b • The difference when b is subtracted from a • The product of a and b
# • The quotient when a is divided by b • The remainder when a is divided by b • The result of log10 a • The result of a


from math import log10
       
a= int(input("Enter the value of a: "))
b= int(input("Enter the value of b: "))

print(a, "+", b, "is",a+b)
print(a, "-", b, "is",a-b)
print(a, "*", b, "is", a * b)
print(a, "/", b, "is",a/b)
print(a, "%", b, "is",a%b)
print("The base 10 logarithm of", a, "is", log10(a))
       print(a, "ˆ", b, "is", a**b)
# Problem 13 : Write a program that begins by reading a number of cents from the user as an integer. Then your program should compute and display the denominations of the
# coins that should be used to give that amount of change to the shopper. The change should be given using as few coins as possible. Assume that the machine is loaded
# with pennies, nickels, dimes, quarters, loonies and toonies. A one dollar coin was introduced in Canada in 1987. It is referred to as a loonie
# because one side of the coin has a loon (a type of bird) on it. The two dollar coin, referred to as a toonie, was introduced 9 years later. It’s name is derived
# from the combination of the number two and the name of the loonie.


CENTS_PER_TOONIE = 200
CENTS_PER_LOONIE = 100
CENTS_PER_QUARTER = 25
CENTS_PER_DIME = 10
CENTS_PER_NICKEL = 5


       
cents = int(input("Enter the number of cents: "))
#note: Floor division, which ensures that the result of the division is an integer by rounding down, is performed using the // operator.

print(" ", cents // CENTS_PER_LOONIE, "loonies")
cents = cents % CENTS_PER_LOONIE
print(" ", cents // CENTS_PER_QUARTER, "quarters")
cents = cents % CENTS_PER_QUARTER
print(" ", cents // CENTS_PER_DIME, "dimes")
cents = cents % CENTS_PER_DIME
print(" ", cents // CENTS_PER_NICKEL, "nickels")
cents = cents % CENTS_PER_NICKEL


# Problem 14 : Many people think about their height in feet and inches, even in some countries that
# primarily use the metric system. Write a program that reads a number of feet from
#the user, followed by a number of inches. Once these values are read, your program
#should compute and display the equivalent number of centimeters. Hint: One foot is 12 inches. One inch is 2.54 centimeters



IN_PER_FT = 12
CM_PER_IN = 2.54
       

print("Enter your height:")
feet = int(input(" Number of feet: "))
inches = int(input(" Number of inches: "))

cm = (feet * IN_PER_FT + inches) * CM_PER_IN

print("Your height in centimeters is:", cm)




       
