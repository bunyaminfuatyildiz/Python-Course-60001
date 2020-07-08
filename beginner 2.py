'''Ex 1 Create a window that will 
ask the user to enter their 
name. When they click on 
a button it should display 
the message “Hello” and 
their name and change 
the background colour 
and font colour of the 
message box.'''
from tkinter import *
def click():
    name = textbox1.get()
    message = str("Hello " + name)
    textbox2["bg"] = "yellow"
    textbox2["fg"] = "blue"
    textbox2["text"] = message
window = Tk()
window.geometry("500x200")

label1 = Label(text = "Enter your name: " )
label1.place(x = 30, y =20)

textbox1 = Entry(text = "")
textbox1.place( x = 150, y = 20, width = 200 , height = 25)
textbox1.focus()

button1 = Button(text = "Press me", command = click)
button1.place(x = 30, y = 50, width = 120, height = 25)

textbox2 = Message( text = "")
textbox2.place(x = 150 , y = 50, width = 250, height = 35)
textbox2["bg"] = "white"
textbox2["fg"] = "black"
window.mainloop


'''Exer 2 Write a program that 
can be used instead 
of rolling a six-sided 
die in a board game. 
When the user clicks 
a button it should 
display a random 
whole number 
between 1 to 6 
(inclusive)'''

from tkinter import *
import random

def click():
    num = random.randint(1,6)
    answer["text"] = num
window = Tk()
window.title("Roll a dice")
window.geometry("100x120")

button1 = Button(text = "Roll", command = click)
button1.place( x = 30, y = 30, width = 50, height = 25)

answer = Message(text = "")
answer.place( x = 40, y = 70, width = 30, height = 25)

window.mainloop()



'''Exercise  3 Create an SQL database called PhoneBook that 
contains a table called Names with some input'''
import sqlite3
with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS Names(id integer PRIMARY KEY,
firstname text,
surname text,
phonenumber text);""")

cursor.execute(""" INSERT INTO Names(id,firstname,surname,phonenumber)
VALUES("1","Simon","Howels","01223 349752")""")
db.commit()

cursor.execute(""" INSERT INTO Names(id,firstname,surname,phonenumber)
VALUES("2","Karen","Phillips","01954 295752")""")
db.commit()

cursor.execute(""" INSERT INTO Names(id,firstname,surname,phonenumber)
VALUES("3","Darren","Smith","01583 349854")""")
db.commit()

cursor.execute(""" INSERT INTO Names(id,firstname,surname,phonenumber)
VALUES("4","Anne","Jones","01223 349752")""")
db.commit()

db.close()





'''Exercise 5   If the user selects 1, they 
should be able to view the 
entire phonebook. If they 
select 2, it should allow them 
to add a new person to the 
phonebook. If they select 3, it 
should ask them for a 
surname and then display 
only the records of people 
with the same surname. If 
they select 4, it should ask 
for an ID and then delete that 
record from the table. If they 
select 5, it should end the 
program. Finally, it should 
display a suitable message if 
they enter an incorrect 
selection from the menu. 
They should return to the 
menu after each action, until 
they select 5'''

import sqlite3
def viewphonebook():
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)
def addtophonebook():
    newid = int(input("Enter ID: "))
    newfname = input("First name:")
    newsname = input("Enter surname:")
    newpnum  = input("Enter phone number:")
    cursor.execute("""INSERT INTO Names (id,firstname,surname,phonenumber)
VALUES(?,?,?,?)""",(newid,newfname,newsname,newpnum))
    db.commit()

def selectname():
    selectsurname = input("Enter a surname:")
    cursor.execute("SELECT* FROM Names WHERE surname = ?", [selectsurname])
    for x in cursor.fetchall():
        print(x)
def deletedata():
    selectid = int(input("Enter ID:"))
    cursor.execute("DELETE FROM Names Where id =?", [selectid])
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)
    db.commit()

with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()


def main():
    again = "y"
    while again == "y":
        print()
        print("Main Menu")
        print()
        print("1) View Phone book")
        print("2) Add to phone book")
        print("3) Search for surname")
        print("4) Delete person")
        print("5) Quit")
        print()
        selection = int(input("Enter your selecetion: "))
        print()
        if  selection == 1:
            viewphonebook()
        elif selection == 2:
            addtophonebook()
        elif selection == 3:
            selectname()
        elif selection == 4:
            deletedata()
        elif selection == 5:
            again = "n"
        else:
            print("Incorrect selection")
main()
db.close()





'''Exercise 6 - Create a new SQL database called BookInfo that will 
store a list of authors and the books they wrote. 
It will have two tables. The first one should be called 
Authors and contain the author name and birthday;
The second should be called Books and contain
the Id, title, author, date of publication'''

import sqlite3
with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS Authors(
Name text PRIMARY KEY,
PlaceofBirth text); """)

cursor.execute(""" INSERT INTO Authors(Name,PlaceofBirth)
VALUES("Agatha Christie","Torquay")""")
db.commit()

cursor.execute(""" INSERT INTO Authors(Name,PlaceofBirth)
VALUES("Oscar Wilde","Dublin")""")
db.commit()

cursor.execute(""" CREATE TABLE IF NOT EXISTS Books(ID integer PRIMARY KEY,
Title text,
Author text,
DatePublished integer); """)


cursor.execute(""" INSERT INTO Books(ID,Title, Author, DatePublished)
VALUES("1","De Profundis","Oscar Wilde","1905")""")

cursor.execute(""" INSERT INTO Books(ID,Title, Author, DatePublished)
VALUES("2","The Secret Advesary","Agatha Christie","1921")""")







'''Exercise 7 
Using the BookInfo database from 
 exercise 6, display the list of 
authors and their place of birth. Ask 
the user to enter a place of birth and 
then show the title, date published 
and author’s name for all the books 
by authors who were born in the 
location they selected.'''

import sqlite3
with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()
cursor.execute("Select * From Authors")
for x in cursor.fetchall():
    print(x)

print()
location = input("Enter a place of birth:")
print()

cursor.execute("""SELECT Books.Title, Books.DatePublished, Books.Author
FROM Books,Author WHERE Authors.Name=Books.Author And Authors.PlaceofBirth=?""",[location])
for x in cursor.fetchall():
    print(x)
db.close()

                
































    

































