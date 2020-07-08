# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 21:45:34 2020

@author: bunyamin
"""

"""Exercise 1- Write a function named reverseLookup that ﬁnds all of the keys in a dictionary
that map to a speciﬁc value. The function will take the dictionary and the value to
search for as its only parameters. It will return a (possibly empty) list of keys from
the dictionary that map to the provided value.
Include a main program that demonstrates the reverseLookup function as part
of your solution to this exercise. Your program should create a dictionary and then
show that the reverseLookup function works correctly when it returns multiple
keys, a single key, and no keys. Ensure that your main program only runs when
the ﬁle containing your solution to this exercise has not been imported into another
program"""
#solution 1-
##
# Conduct a reverse lookup on a dictionary, finding all of the keys that map to the provided
# value.
#
## Conduct a reverse lookup on a dictionary
# @param data the dictionary on which the reverse lookup is performed
# @param value the value to search for in the dictionary
# @return a list (possibly empty) of keys from data that map to value

def reverseLookup(data, value):
    # Construct a list of the keys that map to value
    keys = []
    # Check each key and add it to keys if the values match
    for key in data:
        if data[key]== value:
            keys.append(key)
    #Return the list  of keys
    return keys
#Demonstrate the reverseLookup function
def main():
    # A dictionary mapping 3 Turkish words to their English equivalents:
    Tren =  {"kahve":"coffee", "kitap":"book", "okul":"school",} 
# Demonstrate the reverseLookup function with 3 cases: One that returns multiple keys,
# one that returns one key, and one that returns no keys
    print("The Turkish word for ’coffee’ is: ", reverseLookup(Tren, "the"))
    print("Expected: [’kahve’]")
    print() 
    print("The Turkish word for ’kitap’ is: ", \
reverseLookup(Tren, "book"))
    print("Expected: [kitap]")
    print()
    print("The Turkish word for ’school’ is: ", \
    reverseLookup(Tren, "school"))
    print("Expected: [okul]")
# Call the main function only if this file has not been imported into another program
if __name__ == "__main__":
    main()
    
"""Exercise 2 : Two Dice Simulation
simulate 1,000 rolls of two dice. Begin by writing a function that simulates 
rolling a pair of six-sided dice.Your function will not take any parameters. 
It will return the total that was rolled on two dice as its only result.Write a main program that uses your function to simulate rolling two six-sided
dice 1,000 times. As your program runs, it should count the number of times that
each total occurs.Then it should display a table that summarizes this data. Express
the frequency for each total as a percentage of the number of rolls performed. Your
program should also display the percentage expected by probability theory for each
total."""
#Solution 2- 
# Simulate rolling two dice many times and compare the simulated results to the results
# expected by probability theory.
from random import randrange
NUM_RUNS = 1000
D_MAX = 6 
# simulate rolling two six-sided dice 
#@return the total from rolling two simulated dice
def twoDice():
    #simulate two dice
    d1= randrange(1, D_MAX + 1)
    d2= randrange(1, D_MAX + 1)
    #Return the total 
    return d1 + d2
# LETS SIMULATE MANY ROLLS AND DISPLAY THE RESULT
def main():
    #Create a dictionary of expected proprtions
    expected = {2:1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, \
                7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, \
                11: 2/36, 12: 1/36}
# Create a dictionary that maps from the total of two dice to the number of occurrences
    counts = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, \
              8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
# In the counts dictionary, each value is initialized to 0. The values in counts are increased as the simulation runs.
# Simulate NUM RUNS rolls, and count each roll
    for i in range(NUM_RUNS):
        t = twoDice()
        counts[t] = counts[t] + 1
        # Display the simulated proportions and the expected proportions
        print("Total   Simulated    Expected")
        print("        Percent      Percent")
        for i in sorted(counts.keys()):
            print("%5d %11.2f %8.2f" % \
                  (i, counts[i] / NUM_RUNS * 100, expected[i] * 100))
# Call the main function
main()           

    
'''Exercise 3: Unique Characters
Create a program that determines and displays the number of unique characters in a
string entered by the user. For example, Hello, World! has 10 unique characters
while zzz has only one unique character.Use a dictionary or set to solve this problem.'''
#Solution 3
# Read the string from the user
s = input("Enter a string: ")
# Add each character to a dictionary with a value of True. Once we are done the number
# of keys in the dictionary will be the number of unique characters in the string.
characters = {}
for ch in s:
    characters[ch] = True
    # Display the result
print("That string contained", len(characters), \
"unique character(s).")

'''Exercise 4 : Check the word couple is an anagram'''
#solution 4
##
# Determine whether or not two strings are anagrams and report the result.
#
## Compute the frequency distribution for the characters in a string
# @param s the string to process
# @return a dictionary mapping each character to its count

def characterCounts(s):
    # Create a new, empty dictionary
    counts = {}
# Update the count for each character in the string
    for ch in s:
        if ch in counts:
            counts[ch] = counts[ch] + 1
    else:
        counts[ch] = 1
# Return the result
    return counts
# Determine if two strings entered by the user are anagrams
def main():
# Read the strings from the user
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")
    # Get the character counts for each string
    counts1 = characterCounts(s1)
    counts2 = characterCounts(s2)
    # Display the result
    if counts1 == counts2:
        print("Those strings are anagrams.")
    else:
        print("Those strings are not anagrams.")
main()


''''Exercise 5- Organize program calculate scrabble scores '''
#Solution 5
#Initialize the dictionary so that it maps from letters to points
points = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, \
"G": 2, "H": 4, "I": 1, "J": 2, "K": 5, "L": 1, \
"M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, \
"S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8,
"Y": 4, "Z": 10}
#Read a word from the user
word = input("Enter a word: ")
#The word is converted to uppercase so that the correct result is computed when the user
#enters the word in upper, mixed or lowercase. This could also be accomplished by
#adding all of the lowercase letters to the dictionary.
# Compute the score for the word
uppercase = word.upper()
score = 0
for ch in uppercase:
    score = score + points[ch]
# Display the result
print(word, "is worth", score, "points.")
   
    
    
    
'''Exercise 6:Display the Head of a File
 Unix-based operating systems usually include a tool named head. It displays the
ﬁrst 10 lines of a ﬁle whose name is provided as a command line argument. Write
a Python program that provides the same behaviour. Display an appropriate error
message if the ﬁle requested by the user does not exist, or if the command line
argument is omitted.
'''
#Answer 6- 
# Display the head (first 10 lines) of a file whose name is provided as a command line argument.
#
import sys
NUM_LINES = 10
# Verify that exactly one command line argument (in addition to the .py file) was supplied
if len(sys.argv) != 2:
    print("Provide the file name as a command line argument.")
quit()
try:
    inf = open(sys.argv[1], "r")
    # Read the first line from the file
    line = inf.readline()
    # Keep looping until we have either read and displayed 10 lines or we have reached the end
# of the file
    count = 0
    while count < NUM_LINES and line != "":
# Remove the trailing newline character and count the line
        line = line.rstrip()
        count = count + 1
        # Display the line
        print(line)
        # Read the next line from the file
        line = inf.readline()
        #Close the file
        inf.close()
    
    
    '''Exercise 7:concatanate multiple files. '''
#Answer 7- 
#
import sys
# Ensure that at least one command line argument (in addition to the .py file) has been provided
if len(sys.argv) == 1:
    print("You must provide at least one file name.")
quit()
# Process all of the files provided on the command line
for i in range(1, len(sys.argv)):
    fname = sys.argv[i]
try:
    # Open the current file for reading
    inf = open(fname, "r")
    for line in inf:
      print(line, end="")
      # Close the file
      inf.close()
except:
# Display a message, but do not quit, so that the program will go on and process any
# subsequent files
    print("Couldn’t open/display", fname)
    
    
#Exercise 8 ---  Create a program that sums all of the numbers entered by the user while ignoring
#any input that is not a valid number.
#SOLUTION 8

# Compute the sum of numbers entered by the user, ignoring non-numeric input.
#
# Read the first line of input from the user
line = input("Enter a number: ")
total = 0
# Keep reading until the user enters a blank line
while line != "":
    try:
        # Try and convert the line to a number
        num = float(line)
# If the conversion succeeds then add it to the total and display it
        total = total + num
        print("The total is now", total)
    except ValueError:
# Display an error message before going on to read the next value
        print("That wasn’t a number.")    
        # Read the next number
    line = input("Enter a number: ")
# Display the total
print("The grand total is", total)

#EXERCISE 9 --Write a program that reads values from the user until a blank line is entered.
#SOLUTION 9-
# Total a collection of numbers entered by the user. The user will enter a blank line to
# indicate that no further numbers will be entered and the total should be displayed.
#
## Total all of the numbers entered by the user until the user enters a blank line
# @return the total of the entered values
def readAndTotal():
    # Read a value from the user
    line = input("Enter a number (blank to quit): ")
    # Base case: The user entered a blank line so the total is 0
    if line == "":
        return 0
    else:
        # Recursive case: Convert the current line to a number and use recursion to read the subsequent lines
        return float(line) + readAndTotal()
# Read a collection of numbers from the user and display the total
def main():
    # Read the values from the user and compute the total
    total = readAndTotal()
    # Display the total
    print("The total of all those values is", total)
#call the main function
main()

#Exercise 10 : Determine whether or not a string entered by the user is a palindrome using recursion.
# Solution 10 : Recursive Palindrome
##
def isPalindrome(s):
    if len(s) <= 1:
        return True
    # Recursive case: The string is a palindrome only if the first and last characters match, and
    # the rest of the string is a palindrome
    return s[0] == s[len(s) - 1] and \
           isPalindrome(s[1 : len(s) - 1])
# Check whether or not a string entered by the user is a palindrome
def main():
    # Read the string from the user
    line = input("Enter a string: ")
    if isPalindrome(line):
        print("That was a palindrome!")
    else:
        print("That is not a palindrome.")
# Call the main function
main()


















