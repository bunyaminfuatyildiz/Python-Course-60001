# After assigning the values of x, y, z  respectively, 12, -2.74 and "Andrew"
"d" % x # shows 12 as an output. It means value stored in x is formated as a decimal (base 10) integer.
"%f" % y # shows -2.75 as a result. it means the value stored in y is formatted as a floating-point number.
"%d and %f" %(x,y) # resuls shows "12 and -2.75". it means the value stored in x is formatted as decimal integer and value stored in y is formatted floating-point number.
".4f" %x #gives result as "12.0000" the value stored in x is formatted as a floating-point number with 4 digits to the right of the decimal point.
"%1f" %y # gives result as "-2.8" the value stored in y is formatted as a floating-point number with 1 digit to the right of the decimal point.
"%10s" %z # gives result as "    Andrew". the value stored in z is formatted as a s tring so that it occupies at least 10 spaces. Because z is longer than the indicated minimum length, the resulting string is equal to z.
"%8i %8i" % (x,y )# give results "  12     -2". both x and y are integers with minimum 9 spaces.


#When working with strings
#Read the names from the user
first = input("Enter the first name:")
last = input("Enter the last name:" )
#Concatenate the strings
both = last + " ," + first
#Display the result
print(both)

# Read the name from the user

first = input ("Enter your first name: " )

#Compute its length
num_chars = len(first)
#Display the result
print("Your first name contains", num_chars, "characters")

#Problem 1:Ask the user if it is raining and convert their answer to lower case 
#so it doesn’t matter what case they type it in. If they answer “yes”, 
#ask if it is windy. If they answer “yes” to this second question, 
#display the answer “It is too windy for an umbrella”, otherwise 
#display the message “Take an umbrella”. If they did not answer yes 
#to the first question, display the answer “Enjoy your day”
raining=input("Is it raining?")
raining= str.lower(raining)
if raining=="yes":
    windy=input("Is it windy?")
    windy=str.lower(windy)
    if windy=="yes":
        print("it is too windy for umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")

#Problem 2: ask a person their name and print out the length of their name

name=input("enter your name")
length= len(name)
print("Your name contains", length ,"words")



#Problem 3: AAsk the user to enter their first name and surname in lower 
#case. Change the case to title case and join them together. 
#Display the finished result

firstname= input("Enter your first name:")
surname=input("Enter your surname in lowercase:")
firstname=firstname.title()
surname=surname.title()
name = firstname+" "+surname
print(name)



#Problem 4: Pig Latin takes the first consonant of a word, 
#moves it to the end of the word and adds on an “ay”. If a word begins with a vowel you just add 
#“way” to the end. For example, pig becomes igpay,banana becomes ananabay, and aadvark becomes 
#aadvarkway. Create a program that will ask the user to enter a word and change it into Pig Latin. 
#Make sure the new word is displayed in lower case.
word = input("Please enter a word:")
first word[0]
length= len(word)
rest = word[1:length]
if first != " a" and first != "e" and first !="i" and first !="u":
    newword=rest+first+"ay"
else:
    newword=word+"way"
print(newword.lower())
    

   
# problem 5: Ask the user to enter a number with lots of decimal places. Multiply 
#this number by two and display the answer.

num=float(input("Enter number with lots of decimals:"))
print(num*2)



# problem 6:Update problem 6 so that it will display the answer to two decimal places.
num=float(input("Enter number with lots of decimals:"))
answer=num*2
print(round(answer,2))

# problem 7:Ask the user to enter an integer that is over 500. Work out the square root of that number and display it to two decimal places.
import math
num=int(input( "enter number over 500"))
answer=math.sqrt(num)
print(round(answer,2))

#Problem 8:Ask the user to enter an integer that is over 500. Work 
#out the square root of that number and display it to two decimal places. 
import math
num=int(input( "enter number over 500"))
answer=math.sqrt(num)
print(round(answer,2))


# problem 9:Display pi (π) to five decimal places.
import math
print(round(math.pi,5))

#Problem 10:Ask the user to enter the radius of a circle (measurement from the centre point to the edge). Work 
#out the area of the circle (π*radius2).
import math
radius=int(input("Enter the radius of the circle:"))
area=math.pi*(radius**2)
print(area)
   
#Problem 11: "Ask for the radius and the depth of a cylinder and work out the total volume (circle 
#area*depth) rounded to three decimal places.

import math
radius = int(input("enter radius")
depth = int(input("Enter depth)
area = math.pi*(radius**2)
volume= area*depth    
print(round(volume,3))

#Problem 12: Ask the user to enter two numbers. Use whole number division to divide 
#the first number by the second and also work out the remainder and 
#display the answer in a user-friendly way (e.g. if they enter 7 and 2 display 
#“7 divided by 2 is 3 with 1 remaining”)
num1=int(input("Enter a number"))
num2=int(input("Enter another number:"))
ans1=num1//num2
ans2=num1%num2
print(num1, "divided by",num2,"is", ans1, "with", "remaining.")
                  

#Problem 13: If the user enters 1, then it should ask them for the length of one of its sides and display the 
#area. If they select 2, it should ask for the base and height of the triangle and display the area. If 
#they type in anything else, it should give them a suitable error message.

print("1) Square")
print("2) Triangle")
print()
menuselection = int(input("Enter a number:"))
if menuselection == 1:
                  side = int(input("Enter the length of one side:"))
                  area= side * side
                  print("The area of your chosen shape is", area)
elif menuselection == 2:
                  base = int(input("Enter the length of the base:"))
                  height = int(input("Enter the height of the triangle:"))
                  area = (base * height)/2
                  print("the area of your chosen shape is", area)
else:
    print("Incorrect option selected")
