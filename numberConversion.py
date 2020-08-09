import tkinter as tk
import random

master = tk.Tk()
master.title("Number Converter")
master.geometry('500x200')
master.configure(background = "teal");

def Take_input(numType):
   print(numType)
   inputs =  int(e1.get())
   if(numType==2):
       output = bin(inputs)
       e2.insert(10, output)
   elif(numType==8):
       output = oct(inputs)
       e3.insert(10, output)
   elif(numType==16):
       output = hex(inputs)
       e4.insert(10, output)
   
def Clear_input(): 	    
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)
    e4.delete(0, tk.END)

tk.Label(master, 
         text="Convert Decimal to Binary, Octal and Hexadecimal ",bg="teal").place(x = 15,y = 3)
tk.Label(master, 
         text="Input Decimal",bg="teal").place(x = 20,y = 30)
tk.Label(master, 
         text="Binary",bg="teal").place(x = 20,y = 70)
tk.Label(master, 
         text="Octal",bg="teal").place(x = 20,y = 110)
tk.Label(master, 
         text="Hexadecimal",bg="teal").place(x = 20,y = 150)         
e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)

e1.place(x = 130,y = 30,width=200,height=30)
e2.place(x = 130,y = 70,width=200,height=30)
e3.place(x = 130,y = 110,width=200,height=30)
e4.place(x = 130,y = 150,width=200,height=30)


btn1 = tk.Button(master,text='Clear',command=Clear_input)
btn1.place(x = 350,y = 30)
btn2 = tk.Button(master,text='Binary', command=lambda :Take_input(2))
btn2.place(x = 350,y = 70)
btn3 = tk.Button(master,text='Octal', command=lambda :Take_input(8))
btn3.place(x = 350,y = 110)
btn3 = tk.Button(master,text='Hexadecimal', command=lambda :Take_input(16))
btn3.place(x = 350,y = 150)

tk.mainloop()