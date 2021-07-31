import datetime as dt, tkinter as tk
from userClass import userClass
from userDict import userDict

testUser = userClass("Karyn", "karynpham@gmail.com")
d = userDict({})
d.addUser(testUser)
dDictionary = d.getDict()
# Start frame
class frame1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        f1 = self.frame
        tk.Label(f1, 
                text="Name").grid(row=1, column=0)
        tk.Label(f1, 
                text="Email Address").grid(row=2, column=0)

        e1 = tk.Entry(f1)
        e2 = tk.Entry(f1)
        e1.grid(row=1, column=1)
        e2.grid(row=2, column=1)

        tk.Label(f1, text="Good {time}, User!".format(time = self.stateOfDay()) + '\n' + "This is R.B.C.K. 's catalogue application." 
            + '\n' + "Please input your name and email address below.").grid(row=0, column = 0, columnspan=3)

        tk.Button(f1, 
                text='Quit', 
                command=master.quit).grid(row=3, 
                                            column=0, 
                                            sticky=tk.N, 
                                            pady=4)
        tk.Button(f1, 
                text='Show', command="").grid(row=3, 
                                                            column=1, 
                                                            sticky=tk.N, 
                                                            pady=4)
        tk.Button(f1, 
                text='Enter', command=self.userVerify(e1.get(),e2.get())).grid(row=3, 
                                                            column=2, 
                                                            sticky=tk.N, 
                                                            pady=4)
    def stateOfDay(self):
    # Checks the state of day
        time = dt.datetime.today().hour
        if (time < 12):
            return "Morning"
        elif(12 <= time < 15):
            return "Afternoon"
        else:
            return "Evening"

     # For returning users, checks for their identification in dictionary
    def userVerify(self, name, email):
        hsh = hash(name + email)
        if (d.isKey(name)):
            user = dDictionary.get(hsh).name
        else:
            #emailVerify(name, email)
            newUser = userClass(name, email)
            d.addUser(newUser)
        return 
    # For new users, checks if email exists before adding them to the dictionary
    def emailVerify(name, email):
        return True

class frame2:
    def __init__(self, master, name):
        self.master = master
        self.frame = tk.Frame(self.master)
        f2 = self.frame
        tk.Label(f2, text="Hello, {name}!".format(name = name) + '\n' + "Please enter your food preferences below." 
            + '\n' + "Be sure to seperate each entry with a comma (ex. chicken, salad).").grid(row=0)
        tk.Label(f2, 
                text="Food Preferences").grid(row=1)
        e1 = tk.Entry(f2)
        e1.grid(row=1, column=1)
        tk.Button(f2, 
                text='Quit', 
                command=master.quit).grid(row=3, 
                                            column=0, 
                                            sticky=tk.W, 
                                            pady=4)
        tk.Button(f2, 
                text='Enter', command="").grid(row=3, 
                                                            column=2, 
                                                            sticky=tk.W, 
                                                            pady=4)
def raise_frame(frame):
    frame.tkraise()

def main():
    master = tk.Tk()  #instantiates a new window
    master.title("Recipes for Broke College Kids")
    app = frame1(master)
    master.mainloop()

if __name__ == '__main__':
    main()

        

































#checks for typos in email ending (i.e. gnail.con and underlines it red)
def spellCheck():
    None

# The welcome page. Asks for name and email.


# Prompts for favorite cuisine (Chinese, Indian, etc...)
def cuisinePreferencesFrame():
    None

# Prompts for key words (chicken, curry, etc...)
# Food Preferences tk.Frame
def foodInfo():
    None