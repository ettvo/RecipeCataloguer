import datetime as dt, tkinter as tk, os, pickle
from userClass import userClass
from userDict import userDict

testUser = userClass("Karyn", "karynpham@gmail.com")
d = userDict()
d.addUser(testUser)
currUser = None

#Application Runner
class Frame0(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        window = tk.Frame(self)
        window.pack(side="top", fill="both", expand=True)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Frame1, Frame2):
            page_name = F.__name__
            frame = F(box=window, master=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.showFrame("Frame1")

    def showFrame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

# Start frame
class Frame1(tk.Frame):

    def __init__(self, box, master):
        tk.Frame.__init__(self, box)
        self.master = master

        # For returning users, checks for their identification in dictionary
        def userVerify(name, email):
            hsh = hash(name + email)
            if (not d.doesExist(hsh)):
                #emailVerify(name, email)
                newUser = userClass(name, email)
                d.addUser(newUser)
            currUser = d.getUser(hsh)
            master.showFrame("Frame2")
        
        tk.Label(self, text="Name").grid(row=1, column=0)
        tk.Label(self, text="Email Address").grid(row=2, column=0)

        e1 = tk.Entry(self)
        e2 = tk.Entry(self)
        e1.grid(row=1, column=1)
        e2.grid(row=2, column=1)

        tk.Label(self, text="Good {time}, User!".format(time = self.stateOfDay()) + '\n' + "This is R.B.C.K. 's catalogue application." 
            + '\n' + "Please input your name and email address below.").grid(row=0, column = 0, columnspan=3)

        tk.Button(self, 
                text='Quit', 
                command=master.quit).grid(row=3, 
                                            column=0, 
                                            sticky=tk.N, 
                                            pady=4)
        tk.Button(self, 
                text='Show', command=lambda: print("showing works!")).grid(row=3, 
                                            column=1, 
                                            sticky=tk.N, 
                                            pady=4)
        tk.Button(self, 
                text='Enter', command=lambda: userVerify(e1.get(),e2.get())).grid(row=3, 
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

    # For new users, checks if email exists before adding them to the dictionary
    def emailVerify(name, email):
        return True

class Frame2(tk.Frame):
    def __init__(self, box, master):
        tk.Frame.__init__(self, box)
        self.master = master
        f2 = self

        def foodInput(str):
            foodPref = str.split(", ")
            for food in foodPref:
                print(food)


        tk.Label(f2, text="Hello, {name}!".format(name = lambda: currUser.getName if (currUser) else "User") + '\n' + "Please enter your food preferences below." 
            + '\n' + "Be sure to seperate each entry with a comma (ex. chicken, salad).").grid(row=0, columnspan=2)
        tk.Label(f2, 
                text="Food Preferences").grid(row=1, column=0)

        e1 = tk.Entry(f2)
        e1.grid(row=1, column=1)
        
        tk.Button(self, 
                text='Quit', 
                command=master.quit).grid(row=3, 
                                            column=0, 
                                            sticky=tk.N, 
                                            pady=4)
        tk.Button(self, 
                text='Show', command=lambda: print("showing works!")).grid(row=3, 
                                                column=1, 
                                                sticky=tk.N, 
                                                pady=4)
        tk.Button(self, 
                text='Enter', command=lambda: foodInput(e1.get())).grid(row=3, 
                                                            column=2, 
                                                            sticky=tk.N, 
                                                            pady=4)
        self.grid()




def main():
    app = Frame0()
    app.title("Recipes for Broke College Kids")
    #app.geometry("500x500")
    app.mainloop()

if __name__ == '__main__':
    main()

'''
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
    None'''