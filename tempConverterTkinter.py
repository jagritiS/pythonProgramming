import tkinter as tk
import random

master = tk.Tk()
master.title("Temperature Converter")
master.geometry('500x200')
master.configure(background = "teal");
def temp_convert_f(text): 
   print('temperature conversion ')
   celius = float(text)
   print('temperature in celcius is ',celius)
   ferenheit = (celius*1.8) +32
   print('temperatire in celcius = {0} and farenheit = {1} is '.format(celius,ferenheit)) 
   return ferenheit 

def temp_convert_c(text): 
   print('temperature conversion ')
   ferenheit = float(text)
   print('temperature in celcius is ',ferenheit)
   celcious = (ferenheit-32) *(5/9)
   print('temperatire in celcius = {0} and farenheit = {1} is '.format(celcious,ferenheit)) 
   return celcious 

def Take_input_f():
   inputs =  e1.get()
   e2.insert(10, temp_convert_f(inputs))

def Take_input_c():
   inputs =  e1.get()
   e2.insert(10, temp_convert_c(inputs))
def Clear_input(): 	    
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)

tk.Label(master, 
         text="Input Temperature",bg="teal").place(x = 20,y = 10)
tk.Label(master, 
         text="Resulted Temperature",bg="teal").place(x = 250,y = 10)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e1.place(x = 20,y = 30,width=200,height=30)
e2.place(x = 250,y = 30,width=200,height=30)


btn1 = tk.Button(master,text='Clear',command=Clear_input)
btn1.place(x = 300,y = 100)
btn2 = tk.Button(master,text='Into Fahrenheit', command=Take_input_f)
btn2.place(x = 30,y = 100)
btn3 = tk.Button(master,text='Into Celcius', command=Take_input_c)
btn3.place(x = 170,y = 100)

tk.mainloop()