#Exercise 1 - Create 2 dimensional list with 4 rows and 3 columns

list = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]



#Exercise 2 - Using the 2 dimensional list from program exercise 1,
#ask the user to select a row and a column and display that value.

list = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]
row = int(input("Select a row:"))
col = int(input("Select a  column:"))
print(list[row][col])
        

#Exersise 3  Using the 2D List from exercise 1, Ask the user which row they would like displayed
#and display just that row. Ask them to enter a new value and add it to the end of the row and display
#the row again.


list = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]
row = int(input("Select a row:"))
print(list[row])
newvalue = int(input("Enter a new number:"))
list[row].append(newvalue)
print(list[row])
        

# Exercise 4 Change your previous program to ask the user which row they want displayed. Display that row.
# Ask which column in that row they want displated and display the value that is held there.
#Ask the user if they want to change the value. If they do ask for a new value and change data.
#Finally display the whole row again,

list = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]
row = int(input("Select a row:"))
print(list[row])
col = int(input("Select a  column:"))
print(list[row][col])
change = input("Do you want to change the value?(y/n)")
if change == "y":
        newvalue = int(input("Enter new value:")
        list[row][col] = newvalue
print(list[row])

#Exercise 5 Ask the user to enter the name, age and shoe size for four 
#people. Ask for the name of one of the people in the list and 
#display their age and shoe size


list = {}
for i in  range (0,4):
     name = input("Enter name")
     age = int(input("Enter age:"))
     shoe = int(input("Enter shoe size:"))
     list[name] = {"Age":age, "Shoe size":shoe}
ask = input("Enter one of the  name to investigate:" )
print(list[ask])

#Exercise 6 - Adapt previous program to display the names and ages of all the people in the list
#but do not show thier shoe size
        



list = {}
for i in  range (0,4):
     name = input("Enter name")
     age = int(input("Enter age:"))
     shoe = int(input("Enter shoe size:"))
     list[name] = {"Age":age, "Shoe size":shoe}
for name in list:
     print((name),list[name]["Age"])          





# Exercise 7 - After gathering the four names, ages and shoe size ask the user to
# enter the name of the person they want ot remove from the list.
# Delete this row from the data and display the other rows on separate lines.                      
                       
list = {}
for i in range(0,4):
     name = input("Enter name")
     age = int(input("Enter age:"))
     shoe = int(input("Enter shoe size:"))
     list[name] = {"Age":age, "Shoe size":shoe}
                       
getrid = input("Who do you want to remove from the list?")
del list[getrid]

for name in list:
    print((name),list[name]["Age"],list[name]["Shoe size"])
                       
                            
    

'''# exercise 8 - Write a new file called “Numbers.txt”.
Add five numbers to the document which are stored
on the same line and only separated by a comma.
Once you have run the program, look in the location where your program is 
stored and you should see that the file has been created. The easiest way to view the contents 
of the new text file on a Windows system is to read it using Notepad.'''
file = open("Numbers.txt","w")
file.write("4, " )
file.write("6, ")
file.write("10, ")
file.write("8, ")
file.write("5, ")
file.close()



'''Exercise 9- Create a new file called “Names.txt”. Add five names to the 
document, which are stored on separate lines. Once you have 
run the program, look in the location where your program is 
stored and check that the file has been created properly'''


file = open("Names.txt","w")
file.write("Bob\n")
file.write("Tom\n")
file.write("Gemma\n")
file.write("Sarah\n")
file.write("Timothy\n")
file.close()



''' Exercise 10 - Open the 
Names.txt file and display the data in Python'''


file = open("Names.txt", "r")
print(file.read())
file.close()







''' Exercise 11 - Open the Names.txt file. Ask the user to input a 
new name. Add this to the end of the file and 
display the entire file. '''
file = open("Names.txt","a")
newname = input("Enter a new name: ")
file.write(newname + "\n")
file.close

file = open("Names.txt", "r")
print (file.read())
file.close



'''Exercise 12 - Display the following menu to the user:Ask the user to enter 1, 2 or 3. If they select 
anything other than 1, 2 or 3 it should display a 
suitable error message.  
 
If they select 1, ask the user to enter a school 
subject and save it to a new file called 
“Subject.txt”. It should overwrite any existing file 
with a new file.  
 
If they select 2, display the contents of the 
“Subject.txt” file.  
 
If they select 3, ask the user to enter a new 
subject and save it to the file and then display 
the entire contents of the file.  
 
Run the program several times to test the 
options'''



print ("1) create a new file")
print ("2) display the file")
print ("3) add a new item to the file")
selection = int (input( "Make a selection 1,2, or 3:"))
if selection == 1:
                        subject = input("Enter a school subject: ")
                        file = open("Subject.txt","w")
                        file.write(subject + "\n")
                        file.close()
elif selection == 2:
                        file = open("Subject.txt", "r")
                        print(file.read())
elif selection == 3:
                        file =open("Subject.txt", "a")
                        subject= input("Enter a school subject: ")
                        file.write(subject +"\n")
                        file.close()
                        file = open("Subject.txt","r")
                        print(file.read())
else:
                        print("Invalid option")                       




                       



''' Exercise 13: Using the Names.txt file you created
earlier, display the list of names in Python.
Ask the user to type in one of the names and then
save all the names except the one they entered into
a new file called Names2.txt. '''

file = open("Names.txt", "r")
print(file.read())
file.close()

file = open("Names.txt", "r")
selectedname = input("Enter a name from the list: " )
selectedname = selectedname + "\n"
for row in file:
    if row != selectedname:
        file = open("Names2.txt","a")
        newrecord = row
        file.write(newrecord)
        file.close()
file.close()
                       




'''exercise 14 Create a .csv file
that contain book, author , year released
Call it “Books.csv”.'''

import csv
file = open("Books.csv", "w")
newrecord = "To Kill A Mockingbird, Harper Lee, 1960\n"
file.write(str(newrecord))
newrecord = "A Brief History of Time, Stephen Hawking, 1988\n"
file.write(str(newrecord))
newrecord = "The Man Who Mistook His Wife for a Hat. Oliver Sacks, 1985\n"
file.write(str(newrecord))
newrecord = "Pride and Prejudice, Jane Austen, 1813\n"
file.write(str(newrecord))
file.close()

''' exercise 14.1 Using the Books.csv file 
from program 111, ask 
the user to enter another 
record and add it to the 
end of the file. Display 
each row of the .csv file 
on a separate line.'''
                       
file =open("Books.csv", "a")
title = input ("Enter a title:")
author = input ("enter author:")
year = input("enter the year of book:")
newrecord = title + "," + author + "," + year + "\n"                      
file.write(str(newrecord))
file.close()

file = open("Books.csv" , "r")
for row in file:
            print(row)
file.close()






                       



'''exercise -15  Using the Books.csv file, ask the user how many records 
they want to add to the list and then allow them to add 
that many. After all the data has been added, ask for an 
author and display all the books in the list by that author. 
If there are no books by that author in the list, display a 
suitable message. '''                      

import csv
num = int(input("How many books do you want to add to the list?"))
file = open("Books.csv", "a")
for x in range(0,num):
                       title = input("enter a title:")
                       author = input("enter author:")
                       year = input("enter the year:")
                       newrecord = title + "," +author+","+year+"\n"
                       file.write(str(newrecord))
file.close()
searchauthor = input("Enter an authors name to search for:")
file= open("Books.csv", "r")
count = 0
for row in file:
                       if searchauthor in str(row):
                           print(row)
                           count = count +1
if count == 0 :
                       print("there are no books of this author in our list.")
file.close()                       
    



'''exercise 16 - Using the Books.csv file, display the data in 
the file along with the row number of each'''

import csv
file = open("Books.csv","r")
x = 0
for row in file:
                       display = "Row:" + str(x) + " - " + row
                       print(display)
                       x = x+1
                       







'''Exercise 17 - Import the data from the Books.csv file into a list. Display the 
list to the user. Ask them to select which row from the list 
they want to delete and remove it from the list. Ask the user 
which data they want to change and allow them to change it. 
Write the data back to the original .csv file, overwriting the 
existing data with the amended data '''



import csv
file = list(csv.reader(open("Books.csv")))
Booklist=[]
for row in file:
                       Booklist.append(row)
x = 0
for row in Booklist:
                       display = x, Booklist[x]
                       print(display)
                       x = x+1
getrid = int(input("Enter a row number to delete:"))
del Booklist[getrid]

x= 0
for row in Booklist:
                       display = x, Booklist[x]
                       print(display)
                       x = x+1
alter = int(input("entera row number to change:")
x = 0
for row in Booklist[alter]:
            display = x,Booklist[alter][x]
            print(display)
            x = x+1
part = int(input("which part do you want to change?"))
newdata= input("enter new data:")
Booklist[alter][part] = newdata
print(Booklist[alter])
file = open("Books.csv", "w")
x = 0
for row in Booklist:
            newrecord = Booklist[x][0] + "," + Booklist[x][1]"," + Booklist[x][2] + "\n"
            file.write(newrecord)
            x = x+1
            file.close()

'''Exercise 18 - Define a subprogram that will ask the user to
enter a number and save it as the variable 
“num”. Define another subprogram that will 
use “num” and count from 1 to that number.'''
def ask_value():
    num = int(input("Enter a number:")
    return num
def count(num):
              n = 1
              while n<= num:
              print(n)
              n = n+1
def main():
              num = ask_value()
              count(num)
main()
 

        

'''Exercise 19Define a subprogram 
that will ask the user to 
pick a low and a high 
number, and then 
generate a random 
number between those 
two values and store it in 
a variable called 
“comp_num”. 
 
Define another 
subprogram that will 
give the instruction “I am 
thinking of a number…” 
and then ask the user to 
guess the number they 
are thinking of.  
 
Define a third 
subprogram that will 
check to see if the 
comp_num is the same 
as the user’s guess. If it 
is, it should display the 
message “Correct, you 
win”, otherwise it should 
keep looping, telling the 
user if they are too low or 
too high and asking them 
to guess again until they 
guess correctly.'''

import random
def pick_num():
    low = int(input("Enter the bottom of the range:"))
    high = int(input("enter top range:"))
    comp_num = random.randint(low,high)
    return comp_num
def first_guess():
    print("i am thinking of a number....")
    guess = int(input( "what i am thinking of?")
    return guess
def check_answer(comp_num,guess):
                try_again = True
                while try_again = True:
                if comp_num == guess:
                print(Correct, you win.")
                try_again = False
                elif comp_num > guess:
                      guess = int(input("Too low, try again:")
                else:
                                  guess = int(input("Too high, try again:")
def main():
                                              comp_num = pick_num()
                                              guess = first_guess()
                                              check_answer(comp_num,guess)
main()

                       
























                       

                       
