from tkinter import *
from tkinter import ttk
window = Tk()
window.title("User Registration")
window.geometry('300x300')
window.configure(background = "teal");
  # create a Form label 
heading = Label(window, text="Register Here !", bg="teal").grid(row = 0,column = 1,ipadx="10")
a = Label(window ,text = "First Name",bg="teal").grid(row = 2,column = 0,ipadx="10")
b = Label(window ,text = "Last Name",bg="teal").grid(row = 3,column = 0,ipadx="10")
c = Label(window ,text = "Email Id",bg="teal").grid(row = 4,column = 0,ipadx="10")
d = Label(window ,text = "Contact Number",bg="teal").grid(row = 5,column = 0,ipadx="10")
s= Label(window ,text = "",bg="teal").grid(row = 6,column = 0)
a1 = Entry(window).grid(row = 2,column = 1)
b1 = Entry(window).grid(row = 3,column = 1)
c1 = Entry(window).grid(row = 4,column = 1)
d1 = Entry(window).grid(row = 5,column = 1)
def clicked():
   res = "Welcome to " + txt.get()
   lbl.configure(text= res)
btn = ttk.Button(window ,text="Submit").grid(row=7,column=1)

window.mainloop()
