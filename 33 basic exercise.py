
#exercise 1 - make a turtle move on pentegram
import turtle
turtle.shape("turtle")
for i in range(0,5):
    turtle.forward(100)
    turtle.right(72)
turtle.exitonclick()


# Exercise 2-Draw a square.
import turtle
for i in range(0,4):
    turtle.forward(100)
    turtle.right(90)
turtle.exitonclick()    



# Exercise 3 - Draw a triangle
import turtle
for i in range(0,3):
    turtle.forward(100)
    turtle.left(120)
turtle.exitonclick()
#Exercise 4 - Draw a circle
import turtle
for i in range(0,360):
    turtle.forward(1)
    turtle.right(1)
turtle.exitonclick()    


#Exercise 5- Draw three square in a gap between each.
#Fill them using three different colours.
import turtle
turtle.color("black", "red")
turtle.begin_fill()
for i in range(0,4):
    turtle.forward(70)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.begin.fill()
turtle.pendown
turtle.color("black","yellow")
for i in range(0,4):
    turtle.forward(70)
    turtle.right(90)
turtle.penup()
turtle.endfill()
turtle.forward(100)

turtle.pendown()
turtle.color("black","green")
turtle.begin.fill()
for i in range (0,4):
    turtle.forward(70)
    turtle.right(90)
turtle.end_fill()

turtle.exitonclick()

# Exercise 6 - Draw a five-pointed star
import turtle
for i in range(0,5):
    turtle.forward(100)
    turtle.right(144)
turtle.exitonclick()



#Exercise 8 Draw an octagon that uses a different colour (randomly selected from a list of six possible colours) for each line.
import turtle
import random
turtle.pensize(3)

for i in range (0,8):
    turtle.color(random.choice(["red","blue","yellow","green","pink","orange"]))
    turtle.forward(50)
    turtle.right(45)
turtle.exitonlclick()



#Exercise 9- Draw more complex pattern

import turtle
import random
for x in range(0,10):
    for i in range (0,8):
        turtle.forward(50)
        turtle.right(45)
    turtle.right(36)
turtle.hideturtle()
turtle.exitonclick()





#Exercise 10-Draw a pattern that will change each time the program is run. Use the random function to pick 
#the number of lines, the length of each line and the angle of each turn

import turtle
import random
lines= random.randint(5,20)
for x in range(0,lines):
    length=random.randint(25,100)
    rotate= random.randint(1,365)
    turtle.forward(length)
    turtle.right(rotate)
turtle.exitonclick()





#Exercise 11 Create a tuple containing the names of five countries and display the whole tuple. Ask 
#the user to enter one of the countries that have been shown to them and then display 
#the index number (i.e. position in the list) of that item in the tuple
country_tuple = ("France", "England", "Spain", "Germany", "Turkey")
print(country_tuple)
print()
country = input("Please enter one of the countries from above:")
print(country, "has index number", country_tuple.index(country))


#Exercise 12 - Add to program on exercise 11 to ask the user to enter a number and display the country in that position.
country_tuple = ("France", "England", "Spain", "Germany", "Turkey")
print(country_tuple)
print()
country = input("Please enter one of the countries from above:")
print(country, "has index number", country_tuple.index(country))
print()
num = int(input("Enter a number between 0 and 4: "))
print(country_tuple[num])



'''Exercise 13- Create a list of two sports. Ask the 
user what their favourite sport is and 
add this to the end of the list. Sort the 
list and display it'''
sports_list = [ "soccer", "football"]
sports_list.append(input(" Add one of your favourite sport:"))
sports_list.sort()
print(sports_list)




'''Exercise 14- Create a list of six school subjects. Ask the user which of these 
subjects they don’t like. Delete the subject they have chosen from the 
list before you display the list again.'''

subject_list = ["maths", "english", "computing","history","science", "spanish"]
print(subject_list)
dislike = input("Which of these subjects do you dislike? ")
getrid = subject_list.index(dislike)
del subject_list[getrid]
print(subject_list)



'''Exercise 15 - Ask the user to enter four of their favourite foods and store them in a dictionary so that they are indexed with numbers starting 
from 1.Display the dictionary in full, showing the index number and the item. Ask them which they want to get rid of and remove it from the list.
Sort the remaining data and display  the dictionary '''
food_dictionary = {}
food1 = input("Enter a food you like: ")
food_dictionary[1]= food
food2 = input("Enter another food you like:")
food_dictionary[2] = food2
food3 = input("Enter a third food you like:")
food_dictionary[3] = food 3
food4 = input("Enter one last food you like:")
food_dictionary[4] = food4
print(food_dictionary)
dislike = int(input("which of these do you want to get rid of ? ")
del food_dictionary[dislike]
print(sorted(food_dictionary.values()))
              





''' Exercise 16 -Create a list of four three-digit 
numbers. Display the list to the user, showing each item from 
the list on a separate line. Ask the user to enter a three-digit 
number. If the number they have typed in matches one in 
the list, display the position of that number in the list, 
otherwise display the message “That is not in the list”'''

nums = [123,345,234,765]
for i in nums:
    print(i)
selection = int(input("Enter a number from the list:"))
if selection in nums:
              print(selection,"is in position", nums.index(selection))
else:
              print("that is not in the list")







''' Exercuse 17- Ask the user to enter the names of three people they want to 
invite to a party and store them in a list. After they have entered 
all three names, ask them if they want to add another. If they do, 
allow them to add more names until they answer “no”. When 
they answer “no”, display how many people they have invited to 
the party'''
name1 = input("Enter a name of somebody you want to invite to your party:")
name2 = input("Enter another name:")
name3 = input("Enter a third name:")
party = [name1,name2,name3]
another = input(" do you want to invite another person (y/n):")
while another == "y":
                newname=party.append(input("enter another name:"))
                another = input(" do you want to invite another person (y/n):")

print("You have", len(party), "people coming to your party")





'''Exercise 18-Create a list containing the titles of 
four TV programmes and display 
them on separate lines. Ask the 
user to enter another show and a 
position they want it inserted into 
the list. Display the list again, 
showing all five TV programmes in 
their new positions.'''
tv = ["HIMYM", "Breaking Bad", "Prison Break", "South Park"]
for i in tv:
    print(i)
print()
newtv = input("Enter another TV show:")
position = int(input("Enter a number between 0 and 3:"))
tv.insert(position,newtv)
for i in tv:
    print(i)




'''Exercise 19- Ask the user to enter their 
first name and then display  the length of their first name. 
Then ask for their surnameand display the length of 
their surname. Join their firstname and surname togetherwith a space between and 
display the result. Finally,  display the length of their full 
name (including the space)'''



fname = input("Enter your first name:")
print("That has", len(fname),"characters in it")
sname = input("Enter your surname:")
print("That has", len(sname), "characters in it")
name = fname+ " " + sname
print("Your full name is", name)
print("That has", len(name), "characters in it")






'''Exercise 20- Ask the user to type in their favourite school subject. 
Display it with “-” after each letter, e.g. S-p-a-n-i-s-h-.'''

subject = input("Enter your favourite school subject:")
for letter in subject:
    print(letter, end= "-")

                

'''Exercise 21 - Show the user a line of text from your favourite poem 
and ask for a starting and ending point. Display the 
characters between those two points. '''

poem = "Oh, i wish i'd looked after me teeth,"
print(poem)
start = int(input("Enter a starting number:"))
end = int(input("Enter an end number:"))
print(poem[start:end])








''' Exercise 22 - Ask the user to type in a word in upper case. If they 
type it in lower case, ask them to try again. Keep 
repeating this until they type in a message all in 
uppercase.'''
msg= input("Enter a message in uppercase:")
tryagain = False
while tryagain == False:
    if msg.isupper():
        print("Thank you")
        tryagain = True
    else:
        print("Try again, use capslock")
        msg = input("Enter a message in uppercase:")
        






''' Exercise 23 - Ask the user to type in their 
postcode. Display the first 
two letters in uppercase.'''

postcode = input("Enter your postcode:")
start = postcode[0:2]
print(start.upper())
 





''' Exercise 24 - Ask the user to type in their name 
and then tell them how many vowels 
are in their name. '''

name = input("Enter your name:")
count = 0
nam = name.lower()
for x in name:
    if x=="a" or x == "e" or x=="i" or x=="o" or x == "u":
        count= count + 1
print("Vovels = ", count)



''' Exercise 25 -  Ask the user to enter a new password. Ask 
them to enter it again. If the two passwords 
match, display “Thank you”. If the letters are 
correct but in the wrong case, display the 
message “They must be in the same case”, 
otherwise display the message “Incorrect”. '''

pswd1 = input("Enter a password:")
pswd2 = input("Enter it again:")
if pswd1 == pswd2 :
    print("Thank you")
elif pswd1.lower() == pswd2.lower():
    print("They must be the same case")
else:
    print("Incorrect")





''' Exercise 26 - Ask the user to type in a word and then 
display it backwards on separate lines.'''
word = input("Enter a word:")
length = len(word)
num = 1
for x in word:
    position = length - num
    letter = word[position]
    print(letter)
    num = num + 1
    

''' Exercise 27 - 
Create an array which will store a list of integers. 
Generate five random numbers and store them in 
the array. Display the array (showing each item on 
a separate line).'''

from array import *
import random
nums = array('i',[])
for i in range(0,5):
    num = random.randint(1,100)
    nums.append(num)
for i in nums:
    print(i)



               
''' Exercise 28- Create an array which contains 
five numbers (two of which 
should be repeated). Display 
the whole array to the user. Ask 
the user to enter one of the 
numbers from the array and 
then display a message saying 
how many times that number 
appears in the list.'''

from array import *
nums = array('i',[])
while len(nums) < 5:
    num = int(input("Enter a number between 10 and 20:"))
    if num >= 10 and num <= 20:
              nums.append(num)
    else:
        print("Outside the range")
              
for i in nums:
              print (i)





'''Exercise 29 Create two arrays (one 
containing three numbers that 
the user enters and one 
containing a set of five random 
numbers). Join these two arrays 
together into one large array. 
Sort this large array and display 
it so that each number appears 
on a separate line'''
from array import *
nums = array('i', [5,7,9,2,9])
for i in nums:
              print(i)
num = int(input("Enter a number:"))
if nums.count(num)== 1:
    print(num, "is in the list once")
else:
    print(num, " is in the list", nums.count(num), "times")

              








              

''' Exercise 30 Create two arrays (one 
containing three numbers that 
the user enters and one 
containing a set of five random 
numbers). Join these two arrays 
together into one large array. 
Sort this large array and display 
it so that each number appears 
on a separate line'''

from array import *
import random

num1 = array('i',[])
num2 = array('i',[])
for i in range(0,3):
    num = int(input("Enter a number:"))
    num1.append(num)
for i in range(0,5):
    num = random.randint(1,100)
    num2.append(num)
num1.extend(num2)
num1 = sorted(num1)

for i in num1:
    print(i)
    






              




''' Exercise 31 Ask the user to enter five 
numbers. Sort them into order 
and present them to the user. 
Ask them to select one of the 
numbers. Remove it from the 
original array and save it in a 
new array '''

from array import *
nums = array('i',[])
for i in range(0,5):
    num = int(input("Enter a number:"))
    nums.append(num)
nums = sorted(nums)

for i in nums:
    print(i)

num = int(input(" Select a number from the array:"))
if num in nums:
    nums.remove(num)
    num2 = array('i',[])
    num2.append(num)
    print(nums)
    print(num2)
else:
    print("That is not a value in the array")










''' Exercise 32 Display an array of five 
numbers. Ask the user to 
select one of the numbers. 
Once they have selected a 
number, display the 
position of that item in the 
array. If they enter 
something that is not in 
the array, ask them to try 
again until they select a 
relevant item.'''







''' Exercise 32 Display an array of five 
numbers. Ask the user to 
select one of the numbers. 
Once they have selected a 
number, display the 
position of that item in the 
array. If they enter 
something that is not in 
the array, ask them to try 
again until they select a 
relevant item.'''

from array import *
nums = array('i',[4,6,8,2,5])

for i in nums:
    print(i)
num = int(input("select one of the numbers:"))

tryagain = True
while tryagain == True:
    if num in nums:
        print("This is in position", nums.index(num))
        tryagain = False
    else:
        print("not in array")
        num = int(input("Select one of the numbers:"))
        



''' exercise 33             
Create an array of five numbers 
between 10 and 100 which each have 
two decimal places. Ask the user to 
enter a whole number between 2 and 5. 
If they enter something outside of that 
range, display a suitable error message 
and ask them to try again until they 
enter a valid amount. Divide each of the 
numbers in the array by the number the 
user entered and display the answers 
shown to two decimal places'''

from array import *
import math
nums = array('f', [34.75, 27.23, 99.58, 45.26, 28.65])
tryagain = True
while tryagain == True :
    num = int(input("Enter a number between 2 and 5:"))
    if num <2 or num>5:
        print("Incorrect value,try again.")
    else:
        tryagain = False
for i in range(0,5):
    ans = nums[i]/num
    print(round(ans,2))
    



              
              

              
