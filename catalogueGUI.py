import datetime as dt
from tkinter import *

time = dt.datetime.today().hour
name = "Karyn" #input dictionary later

# Checks the state of day
if (time < 12):
    greeting = "Morning"
elif(12 < time < 15):
    greeting = "Afternoon"
else:
    greeting = "Evening"

window = Tk()  #instantiates a new window
window.title("Recipes for Broke College Kids")   
window.geometry("500x500")

wintext =  Text(window)  #instantiates wintext
wintext.insert( INSERT, "Good {time}, {name}!".format(time = greeting, name = name))
wintext.insert( END, '\n' + "This is R.B.C.K. 's catalogue application." + '\n' + "Please input your name and email address below.") 

lName = Label(window, text="First Name")
lSurname = Label(window, text="Last Name")

e1 =  Entry(window)
e2 =  Entry(window)

wintext.pack
lName.pack
lSurname.pack
e1.pack
e2.pack

window.mainloop()