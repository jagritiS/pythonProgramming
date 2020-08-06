import tkinter as tk
import random

master = tk.Tk()
master.title("Text Encryption")
master.geometry('500x500')
master.configure(background = "teal");
def encrypt(text): 
    result = "" 
    s = random.randint(1,9)    
    # traverse text 
    for i in range(len(text)): 
        char = text[i]   
        # Encrypt uppercase characters 
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65)   
        # Encrypt lowercase characters 
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97)   
    return result 

def Take_input():
   inputs =  e1.get()
   e2.insert(10, encrypt(inputs))
def Clear_input(): 	    
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)

tk.Label(master, 
         text="Plain Text",bg="teal").place(x = 20,y = 10)
tk.Label(master, 
         text="Encrypted Text",bg="teal").place(x = 250,y = 10)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e1.place(x = 20,y = 30,width=200,height=100)
e2.place(x = 250,y = 30,width=200,height=100)


btn1 = tk.Button(master,text='Clear',command=Clear_input)
btn1.place(x = 150,y = 150)
btn2 = tk.Button(master,text='Encrypt', command=Take_input)
btn2.place(x = 30,y = 150)

tk.mainloop()