#Problem 1-Ask the user to enter their name and then display their name three times
name =input("Hello please write your name ? ")
for i in range (0,3):
   print(name)


#Problem 2- change  problem 1 so that it will ask the user to enter their name and a number and then display their name that number of times.
name = input("Hello please write your name ? ")
number= int(input("Enter a number times you want to hear:"))
for i in range(0,number):
   print(name)


#Problem 3-Ask the user to enter their name and display each letter in their name on a separate line             
name= input("name please")
for i in name:
    print(i)


#Problem 4- Change problem 3 to also ask for a number. Display their name (one letter at a time on each line) and repeat this for the number of times they entered
name= input("name please")
number= int(input("Enter a number times you want to hear:"))
for x in range(0,number):
   for i in name:
      print(i)
      
#Problem 5-Ask the user to enter a number between 1 and 12 and then display the times table for that number.
num=int(input("enter a number betw 1 and 12 :"))
for i in range(1,13):
   answer = i*num
   print(i,"x",num,"=", answer)


#Problem 6-Ask for a number below 50 and then count down from 50 to that number, making sure you show the number they entered in the output.
num=int(input("enter a number below 50"))
for i in range(50,num-1,-1):
   print(i)


#Problem 7-Ask the user to enter their  name and a number. If the number is less than 10, then display their name that number of times; otherwise display the message “Too high” three times.
name = input("Enter your name: ")
num=int(input("Enter a number:"))
if num<10:
    for i in range(0,num):
       print(name)
else:
   for i in range(0,3):
      print("Too high")
      
#Problem 8-Set a variable called total to 0. Ask the user to enter five numbers and after each input ask them if they want that number included. If they do, then add the 
#number to the total. If they do not want it included, don’t add it to the total. After they have entered all five numbers, display the total.

total = 0
for i in range(0,5):
   num = int(input("Enter a number:"))
   ans = input("Do you want this number included? (y/n)")
   if ans=="y":
      total = total+num
print(total)


#Problem 9-Ask which direction the user wants to count (up or down). If they select up, then ask them for the top number and then count from 1 to that number. If they select down, ask 
#them to enter a number below 20 and then count down from 20 to that number. If they entered something other than up or down, display the message “I don’t understand”.
direction = input("Do you want to count up or down? (u/d)")
if direction == "u":
   num = int(input("What is the top number:"))
   for i in range(1,num+1):
      print(i)
elif direction == "d":
   num=int(input("Enter a number below 20:"))
   for i in range(20,num-1,-1):
      print(i)
else:
    print("What the fuck ?")

#Problem 10-Ask how many people the user wants to invite to a party. If they enter a number below 10, ask for the names and after each name display “[name] has been invited”. If they 
#enter a number which is 10 or higher, display the message “Too many people”.
num = int(input("How many friends do you want invite the party?"))
if num < 10:
   for i in range(0,num):
      name = input("Enter a name:")
      print(name, "has been invited")
else:
   print("Too many people")

#PROBLEM 11- 045   Set the total to 0 to start with. While the total is 50 or less, ask the user to input a number. Add that number to the total and 
#print the message “The total is… [total]”. Stop the loop when the total is over 50.
total = 0
while total<= 50:
   num = int(input("Enter a number:"))
   total= total+num
   print("The total is...", total)
   
#PROBLEM 12-Ask the user to enter a number. Keep asking until they enter a value over 5 and then display the message 
#the last number you entered was a [number] and stop the program

num = 0 
while num <=5:
    num= int(input("enter a number:"))
print("the last number you entered was a", num )

#PROBLEM 13- Ask the user to enter a number and then enter another number.. Add these two numbers together and then ask if they want to add another number.
# If they enter “y", ask them to enter another number and keep adding numbers until they do not answer “y”. 
# Once the the totaloop has stopped,display the total. display the total. 
num1=int(input("Enter a number:"))
total = num1
again = "y"
while again =="y":
    num2 = int(input("Enter another number:"))
    total = total +num2
    again = input("Do you want to add another number?(y/n)")
print("The total is", total)    
   
#PROBLEM 14-Ask for the name of somebody the user wants to invite to a party. After this, display the message “[name] has 
#now been invited” and add 1 to the count. Then ask if they want to invite somebody else. Keep repeating this until they no longer want to invite anyone else to the 
#party and then display how many people they have coming to the party.                    
again = "y" 
count = 0 
while again =="y":
    name=input("Enter a name to invite:")
    print(name, " has now been invited")
    count = count +1 
    again = input("Do you want to invite somebody else? (y/n)")
print("You have", count,"people coming to your party")


# PROBLEM 15- Create a variable called compnum and set the value to 50. Ask the user to enter a number. While their guess is not the same as the 
# compnum value, tell them if their guess is too low or too high and ask them to have another guess. If they enter the same value as 
# compnum, display the message “Well done, you took [count] attempts”.
compnum = 50 
guess = int(input("Can you guess the number  I am thinking of?"))
count = 1 
while guess != compnum:
    if guess < compnum:
        print("Too low")
    else:
        print("Too high")
    count = count +1
    guess = int(input("Have another guess:"))
print("Well done, you took", count, "attempts")
        

#PROBLEM 16-Ask the user to enter a number between 10 and 20. If they enter a value under 10, display the message “Too low” and ask them to try again. If they enter a value above 20, 
# display the message “Too high” and ask them to try again. Keep repeating this until they enter a value that is between 10 and 20 and then display the message “Thank you”.
num = int(input("Enter a number between 10 and 20:"))
while num < 10 or num >20:
    if num<10:
        print("Too low")
    else: 
        print("Too high")
    num = int(input("Try again:"))
print("Thank you")


#PROBLEM 17-Display a random integer between 1 and 100 inclusive.
import random
num = random.randint(1,100)
print(num)


#PROBLEM 18-   Display a random fruit from a list of five fruits.
import random
Fruit= random.choice(["apple", "orange", "grape", "banana", "strawberry"])
print(fruit)

#PROBLEM 19-Randomly choose either heads or tails (“h” or “t”). Ask the user to make their choice. If their choice is the same as the randomly selected value,
#display the message “You win”, otherwise display “Bad luck”. At the end, tell the user if the computer selected heads or tails.

import random
coin=random.choice(["h","t"])
guess= input("Enter (h)eads or (t)ails:")
if guess == coin:
   print("you win")
else:
   print("Bad luck")
if coin == "h":
   print("It was heads")
else:
   print("it was tails")

#PROBLEM 20- Randomly choose a number between 1 and 5. Ask the user to pick a number. If they guess correctly, display the message “Well done”, 
#otherwise tell them if they are too high or too low and ask them to pick a second number. If they guess correctly on their second guess, display “Correct”, otherwise display “You lose”.
import random
num = random.randint(1,5)
guess= int(input("Enter a number btw 1-5:"))
if guess == num:
   print("Well done")
elif guess > num:
   print("too high")
   guess=int(input("Guess again:"))
   if guess == num:
      print("Correct")
   else:
      print("You lose")
elif guess<num:
   print("too low")
   guess=int(input("guess again:"))
   if guess == num:
      print("Correct")
   else:
      print("You lose")



#PROBLEM 21-Randomly pick a whole number between 1 and 10. Ask the user to enter a number and 
#keep entering numbers until they enter the number that was randomly picked.
import random
num = random.randint(1,10)
guess= int(input("Enter a number btw 1-10:"))
while guess == num:
   print("well done")
else:
    guess= int(input("you re wrong, Enter another number:"))
if guess== num :
    print("well done")
else:
    print("you have failed to forecast")

#Problem 22- Make a maths quiz that asks five questions by randomly generating two whole numbers to make the question 
#(e.g. [num1] + [num2]). Ask the user to enter the answer. If they get it right add a point to their score. At the end of the quiz,
#tell them how many they got correct out of five.

import random
score= 0
for i in range (1,6):
   num1 = random.randint(1,50)
   num2 = random.randint(1,50)
   correct = num1 + num2
   print(num1, "+", num2,"=")
   answer = int(input("Your answer:"))
   print()
   if answer == correct:
      score = score +1
print(" You scored", score, "out of 5")












