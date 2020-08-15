import tkinter as tk
import random
import string
import urllib.request
import mysql.connector


master = tk.Tk()
master.title("Jags Mini URL")
master.geometry('500x200')
master.configure(background="teal");
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Sunway"
)
print(mydb)
mycursor = mydb.cursor()


def Take_input(urls):
    print(urls)
    inputs = e1.get()
    output = shortens(inputs)
    e2.insert(10, output)
def shortens(inputs):
    N = 5
    res = "jags.mini/"+''.join(random.choices(string.ascii_lowercase+string.digits, k=N))
    print("The generated random string : " + str(res))
    output = dbSetup(inputs,str(res))
    print("the output from database is ",output)
    apiurl = "http://tinyurl.com/api-create.php?url="

    tinyurl = urllib.request.urlopen(apiurl + inputs).read()
    return (str(tinyurl.decode("utf-8")))

def dbSetup(orgnlUrl,shrtUrl):
    mycursor.execute("SHOW TABLES LIKE 'urls'")
    result = mycursor.fetchone()
    if result:
        print("Table exists")
    else:
        # there are no tables named "tableName"
        mycursor.execute("CREATE TABLE urls (id int(10) PRIMARY KEY AUTO_INCREMENT, orginal_url VARCHAR(255), short_url VARCHAR(255))")

    sql = "INSERT INTO urls (orginal_url, short_url) VALUES (%s, %s)"
    val = (orgnlUrl,shrtUrl)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    sql = "SELECT * FROM urls where orginal_url = %s"
    oURL = (orgnlUrl,)
    mycursor.execute(sql, oURL)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    return x

def Clear_input():
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)

tk.Label(master,
         text="The URL shortener", bg="teal").place(x=15, y=3)
tk.Label(master,
         text="Input URL", bg="teal").place(x=20, y=30)
tk.Label(master,
         text="Short URL", bg="teal").place(x=20, y=70)

e1 = tk.Entry(master)
e2 = tk.Entry(master)


e1.place(x=130, y=30, width=200, height=30)
e2.place(x=130, y=70, width=200, height=30)


btn1 = tk.Button(master, text='Clear', command=Clear_input)
btn1.place(x=350, y=30)
btn2 = tk.Button(master, text='Shorten', command=lambda: Take_input(2))
btn2.place(x=350, y=70)


tk.mainloop()