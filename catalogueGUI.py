import datetime as dt
from tkinter import *

time = dt.datetime.today().hour
name = ""
master = Tk()  #instantiates a new window
master.title("Recipes for Broke College Kids")

def stateOfDay():
    # Checks the state of day
    if (time < 12):
        return "Morning"
    elif(12 <= time < 15):
        return "Afternoon"
    else:
        return "Evening"

def raise_frame(frame):
    frame.tkraise()

f1 = Frame(master)
f2 = Frame(master)
f3 = Frame(master)
f4 = Frame(master)

for frame in (f1, f2, f3, f4):
    frame.grid(row=0, column=0, sticky='news')

# For new users, checks if email exists
def emailVerification():
    None

# For returning users, checks for their identification in dictionary
def nameVerification():
    None

#checks for typos in email ending (i.e. gnail.con and underlines it red)
def spellCheck():
    None

# The welcome page. Asks for name and email.
# Start Frame
def show_entry_fields():
    print("Name: %s\nEmail Address: %s" % (e1.get(), e2.get()))

def logInfo(name):
    name = name

Label(f1, text="Good {time}, User!".format(time = stateOfDay()) + '\n' + "This is R.B.C.K. 's catalogue application." 
    + '\n' + "Please input your name and email address below.").grid(row=0)

Label(f1, 
        text="Name").grid(row=1)
Label(f1, 
        text="Email Address").grid(row=2)

e1 = Entry(f1)
e2 = Entry(f1)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)

Button(f1, 
        text='Quit', 
        command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=W, 
                                    pady=4)
Button(f1, 
        text='Show', command=show_entry_fields).grid(row=3, 
                                                    column=1, 
                                                    sticky=W, 
                                                    pady=4)
Button(f1, 
        text='Enter', command=lambda:raise_frame(f2)).grid(row=3, 
                                                    column=2, 
                                                    sticky=W, 
                                                    pady=4)

# Prompts for favorite cuisin (Chinese, Indian, etc...)
def cuisinePreferencesFrame():
    None

# Prompts for key words (chicken, curry, etc...)
# Food Preferences Frame
def foodInfo():
    None
Label(f2, text="Hello, {name}!".format(name = name) + '\n' + "Please enter your food preferences below." 
    + '\n' + "Be sure to seperate each entry with a comma (ex. chicken, salad).").grid(row=0)
Label(f2, 
        text="Name").grid(row=1)
e1 = Entry(f2)
e1.grid(row=1, column=1)
Button(f2, 
        text='Quit', 
        command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=W, 
                                    pady=4)
Button(f2, 
        text='Enter', command=foodInfo()).grid(row=3, 
                                                    column=2, 
                                                    sticky=W, 
                                                    pady=4)
raise_frame(f1)
master.mainloop()

'''
Button(f1, text='Go to frame 2', command=lambda:raise_frame(f2)).pack()
Label(f1, text='FRAME 1').pack()

Label(f2, text='FRAME 2').pack()
Button(f2, text='Go to frame 3', command=lambda:raise_frame(f3)).pack()

Label(f3, text='FRAME 3').pack(side='left')
Button(f3, text='Go to frame 4', command=lambda:raise_frame(f4)).pack(side='left')

Label(f4, text='FRAME 4').pack()
Button(f4, text='Goto to frame 1', command=lambda:raise_frame(f1)).pack()'''

