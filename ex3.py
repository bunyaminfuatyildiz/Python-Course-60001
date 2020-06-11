# -*- coding: utf-8 -*-
"""
Created on Thu May 21 13:56:53 2020

@author: bunyamin"""
"""#QUESTION-001:  Compute the Perimeter of a Polygon Begin by reading the
#x and y coordinates for the ﬁrst point on the perimeter of the polygon from the user. 
#Then continue reading pairs of values until the user enters a blank line for the
#x-coordinate. Each time you read an additional coordinate you should compute the
#distance to the previous point and add it to the perimeter.When a blank line is entered
#for the x-coordinate your program should add the distance from the last point back
#to the ﬁrst point to the perimeter. Then the perimeter should be displayed. Sample
#input and output values are shown below. The input values entered by the user are
#shown in bold."""

#ANSWER-001:
##
# Compute the perimeter of a polygon constructed from points entered by the user. A blank line
# will be entered for the x-coordinate to indicate that all of the points have been entered.

from math import sqrt
# Store the perimeter of the polygon
perimeter=0
# Read the coordinate of the first point 
first_x = float(input("Enter the first x-coordinate:"))
first_y = float(input("Enter the first y-coordinate:"))
#provide initial valuesfor prev_x and prev_y
prev_x = first_x
prev_y = first_y
#Read the remaining coordinates
line= input("enter the next x-coordinate(or blank to quit_):")
while line != "" : 
    #Convert the x-coordinate to a number and read the y coordinate
    x= float(line)
    y= float(input("enter the next y-coordinate:"))
    #Compute the distance to the previous point and add it to the perimeter
    dist = sqrt((prev_x - x)**2 + (prev_y-y)**2)
    perimeter = perimeter + dist
    #Set up prev_x and prev_y forthe next loop irweRION
    prev_x = x
    prev_y = y
    #Read the next x-coordinate 
    line = input("Enter the next x-coordinate(blank to quit):")
    # Compute the distance from the last point to the first point and add it to the perimeter
dist = sqrt((first_x - x) ** 2 + (first_y - y) ** 2)
perimeter = perimeter + dist
# Display the result
print("The perimeter of that polygon is", perimeter)



##QUESTION-002Exercise 69:Admission Price
"""A particular zoo determines the price of admission based on the age of the guest.
Guests 2 years of age and less are admitted without charge. Children between 3 and
12 years of age cost $14.00. Seniors aged 65 years and over cost $18.00. Admission
for all other guests is $23.00.Create a program that begins by reading the ages of all 
of the guests in a group from the user, with one age entered on each line. 
The user will enter a blank line to indicate that there are no more guests in the group.
 Then your programshould display the admission cost for the group with an appropriate message.
 The cost should be displayed using two decimal places."""
 
## ANSWER 002 
#Please determine And save the prices 
age=[]
cost=0
print('Enter the ages of members:')
l=(input())
while l!='': 
	age.append(int(l))
	l=input()
for i in age:
	if i<=2:
		cost=cost+0
	elif i>=3 and i<=12:
		cost=cost+14
	elif i>=65:
		cost=cost+18
	else:
		cost=cost+23
if cost==0:
	print('Enter a valid input!!!')
else:
	print('Total cost of admission = $ %.2f'%(cost))

        
"""QUESTION-3 Write a program that implements a Caesar cipher. Allow the user to supply the
message and the shift amount, and then display the shifted message. Ensure that
your program encodes both uppercase and lowercase letters. Your program should
also support negative shift values so that it can be used both to encode messages and
decode messages."""
#ANSWER 003

##
# Implement a Caesar cipher that shifts all of the letters in a message by an amount provided
# by the user. Use a negative shift value to decode a message.
#note: The ord function converts a character to its integer position within the ASCII table. The chr
#function returns the character in the ASCII table at
#the position provided as an argument.
 # Read the message and shift amount from the user
message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))
# Process each character to construct the encrypted (or decrypted) message
new_message = ""
for ch in message:
    if ch >= "a" and ch <= "z":
# Process a lowercase letter by determining its
# position in the alphabet (0 - 25), computing its
# new position, and adding it to the new message
        pos = ord(ch) - ord("a")
        pos = (pos + shift) % 26
        new_char = chr(pos + ord("a"))
        new_message = new_message + new_char
    elif ch >= "A" and ch <= "Z":
# Process an uppercase letter by determining its position in the alphabet (0 - 25),
# computing its new position, and adding it to the new message
            pos = ord(ch) - ord("A")
            pos = (pos + shift) % 26
            new_char = chr(pos + ord("A"))
            new_message = new_message + new_char
    else:
# If the character is not a letter then copy it into the new message
        new_message = new_message + ch
 # Display the shifted message
print("The shifted message is", new_message)


##QUESTION-4 Evaluate whether is a String a Palindrome or not?
##ANSWER 004
 

line = input("Write a string:")

# Assume that it is a palindrome until we can prove otherwise
is_palindrome = True 

'''Check the characters, starting from the ends. Continue until the middle is reached or we have
determined that the string is not a palindrome.'''
i = 0
while i < len(line) / 2 and is_palindrome:
    # If the characters do not match then mark that the string is not a palindrome
    if line[i] != line[len(line) - i - 1]:
        is_palindrome = False
        # Move to the next character
        i = i + 1
        # Display a meaningful output message
if is_palindrome:
    print(line, "is a palindrome")
else:
    print(line, "is not a palindrome")
    
    # QUESTION 5:Greatest Common Divisor of two number
#Answer
    
# Read two positive integers from the user
n = int(input("Enter a positive integer: "))
m = int(input("Enter a positive integer: "))
# Initialize d to the smaller of n and m
d = min(n, m)
# Use a while loop to find the greatest common divisor of n and m
while n % d != 0 or m % d != 0:
    d = d - 1
# Report the result
print("The greatest common divisor of", n, "and", m, "is", d)   
    
   # QUESTION 6: Median of Three Values
# ANSWER Compute and display the median of three values entered by the user. This program includes
# two implementations of the median function that demonstrate different techniques for
# computing the median of three values.
### Compute the median of three values using if statements
# @param a the first value
# @param b the second value
# @param c the third value
# @return the median of values a, b and c
def median(a,b,c):
    if a<b and b<c or a>b and b>c:
        return b
    if b<a and a<c or b>a and a>c:
        return a
    if c<a and b<c or c>a and b>a:
        return c
 ## Compute the median of three values using the min and max functions and a little bit of
# arithmetic
# @param a the first value
# @param b the second value
# @param c the third value
# @return the median of values a, b and c
def alternateMedian(a, b, c):
  return a + b + c - min(a, b, c) - max(a, b, c)
# Display the median of 3 values entered by the user
def main():
    x = float(input("Enter the first value: "))
    y = float(input("Enter the second value: "))
    z = float(input("Enter the third value: "))
    print("The median value is:", median(x, y, z))
    print("Using the alternative method, it is:", \
          alternateMedian(x, y, z))
# Call the main function
main()
 

#QUESTION 7:Center a String in the TerminalWindow
'''Write a function that takes a string, s, as its ﬁrst parameter, and the width of the
window in characters, w, as its second parameter. Your function will return a new
string that includes whatever leading spaces are needed so that s will be centered in
the window when the new string is printed. The new string should be constructed in
the following manner:
    If the length of s is greater than or equal to the width of the window then s should
be returned.
    If the length of s is less than the width of the window then a string containing
(len(s) - w) // 2 spaces followed by s should be returned.
Write a main program that demonstrates your function by displaying multiple
strings centered in the window.'''
#answer
#Center a string of characters within a certain width.
#
WIDTH = 80
## Create a new string that will be centered within a given width when it is printed.
# @param s the string that will be centered
# @param width the width in which the string will be centered
# @return a new copy of s that contains the leading spaces needed to center s
def center(s,width):
# the case a string is too long to center
    if width< len(s):
        return s
    #number of spaces needed and generate the result
    spaces = (width-len(s)) // 2 
    result = " " * spaces+s
    return result
#Demonstrate the center function 
def main():
    print (center ("A Famous Story", WIDTH))
    print(center("by:", WIDTH))
    print(center("Someone Famous", WIDTH))
    print()
    print ("Once upon a time...")
    main()
 
 #QUEST 8: CAPITALIZE LETTERS 
 ## answerrr Capitalize the appropriate characters in a string
# @param s the string that needs capitalization
# @return a new string with the capitalization improved
def capitalize(s):
    # Create a new copy of the string to return as the function’s result
    result = s
    # Capitalize the first non-space character in the string
    pos = 0
    while pos < len(s) and result[pos] == " ":
        pos = pos + 1
    if pos < len(s):
     # Replace the character with its uppercase version without changing any other characters
     result = result[0 : pos] + result[pos].upper() + \
     result[pos + 1 : len(result)]
 # Capitalize the first letter that follows a ‘‘.’’, ‘‘!’’ or ‘‘?’’
pos = 0
while pos < len(s):
    if result[pos] == "." or result[pos] == "!" or result[pos] == "?":
        pos = pos + 1
    # Move past any spaces
while pos < len(s) and result[pos] == " ":
    pos = pos + 1
# If we haven’t reached the end of the string then replace the current character
# with its uppercase equivalent
if pos < len(s):
    result = result[0 : pos] + \
    result[pos].upper() + \
    result[pos + 1 : len(result)]
# Move to the next character
pos = pos + 1
#Capitalize i when it is preceded by a space and followed by a space, period, exclamation
# mark, question mark or apostrophe
pos = 1
while pos < len(s) - 1:
     result[pos - 1] == " " and result[pos] == "i" and \
(result[pos + 1] == " " or result[pos + 1] == "." or \
result[pos + 1] == "!" or result[pos + 1] == "?" or \
result[pos + 1] == "'"):
# Replace the i with an I without changing any other characters
result = result[0 : pos] + "I" + \
result[pos + 1 : len(result)]
pos = pos + 1
return result 

 #QUEST 9:GENERATE RANDOM PASSWORD
 from random import randint
SHORTEST = 7
LONGEST = 10
MIN_ASCII = 33
MAX_ASCII = 126
## Generate a random password
# @return a string containing a random password
def randomPassword():
# Select a random length for the password
randomLength = randint(SHORTEST, LONGEST)
result = ""
for i in range(randomLength):
randomChar = chr(randint(MIN_ASCII, MAX_ASCII))
result = result + randomChar
Return the random password
return result
# Generate and display a random password
def main():
print("Your random password is:", randomPassword())
# Call the main function only if the module is not imported
if __name__ == "__main__":
main()



#QUESTION 10: Sorted OrderWrite a program that reads integers from the user and stores them in a list. Your
#program should continue reading values until the user enters 0.

#ANSWER 10: Display a list of integers entered by the user in ascending order.
# Start with an empty list
data = []
#Read values and add them to list until the user enter 0
num = int(input("Enter an integer (0 to quit): "))
while num != 0:
    data.append(num)
    num = int(input("Enter an integer (0 to quit): "))
  # Sort the values
  data.sort()
  # Display the values in ascending order
print("The values, sorted into ascending order, are:")
for num in data:
print(num)


#QUESTION 11 : CREATE program shows Negatives,Zeros and Positives in order

negatives = []
zeros = []
positives = []
line = input("Enter an integer (blank to quit): ")
while line != "":
    num = int(line)
if num < 0:
    negatives.append(num)
elif num > 0:
    positives.append(num)
else:
    zeros.append(num)
# Read the next line of input from the user
line = input("Enter an integer (blank to quit): ")
# Display all of the negative values, then all of the zeros, then all of the positive values
print("The numbers were: ")
for n in negatives:
    print(n)
for n in zeros:
    print(n)
for n in positives:
    print(n)


#QUESTION 12 Formatting a List  When writing out a list of items in English, one normally separates the items with
#commas. In addition, theword “and” is normally included before the last item, unless
#the list only contains one item. Consider the following four lists
#apples
#apples and oranges
#apples, oranges and bananas
#apples, oranges, bananas and lemons

#ANSWER :
# Display a list of items so that they are separated by commas and the word ‘‘and’’ appears
# between the final two items.
#
## Format a list of items so that they are separated by commas and ‘‘and’’
# @param items the list of items to format
# @return a string containing the items with the desired formatting

def formatList(items):
    # Handle lists of 0 and 1 items as special cases
    if len(items) == 0:
        return "<empty>"
    if len(items) == 1:
        return str(items[0])
    # Loop over all of the items in the list except the last two
    result = ""
    for i in range(0, len(items) - 2):
        result = result + str(items[i]) + ","+str(items[len(items) - 2]) + " and "+str(items[len(items) - 1])
        # Add the second last and last items to the result, separated by ‘‘and’’
        return result
# Read several items entered by the user and display them with nice formatting
def main():
    # Read items from the user until a blank line is entered
    items = []
    line = input("Enter an item (blank to quit): ")
    while line != "":
        items.append(line)
        line = input("Enter an item (blank to quit): ")
    # Format and display the items
    print("The items are %s." % formatList(items))
# Call the main function
main()


#question 13 : RandomLottery Numbers In order to win the top prize in a particular lottery, one must match all 6 numbers
#on his or her ticket to the 6 numbers between 1 and 49 that are drawn by the lottery organizer. Write a program that generates a random selection of 6 numbers for a
#lottery ticket. Ensure that the 6 numbers selected do not contain any duplicates. Display the numbers in ascending order.

##
# Compute random but distinct numbers for a lottery ticket.
#
from random import randrange
MIN_NUM = 1
MAX_NUM = 49
NUM_NUMS = 6
# Use a list to store the numbers on the ticket
ticket_nums = []
# Generate NUM NUMS random but distinct numbers
for i in range(NUM_NUMS):
    rand = randrange(MIN_NUM, MAX_NUM + 1)
    while rand in ticket_nums:
        rand = randrange(MIN_NUM, MAX_NUM + 1)
    # Add the number to the ticket
    ticket_nums.append(rand)
    # Sort the numbers into ascending order and display them
ticket_nums.sort()
print("Your numbers are: ", end="")
for n in ticket_nums:
    print(n, end=" ")
print()

