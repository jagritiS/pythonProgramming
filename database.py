import mysql.connector
#mydb is the database connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Sunway"
)
print(mydb)
mycursor = mydb.cursor()
#check if the table exists and if not then create a table
mycursor.execute("SHOW TABLES LIKE 'students'")
result = mycursor.fetchone()
if result:
    print("Table exists")
else:   
    mycursor.execute("CREATE TABLE students (name VARCHAR(255), address VARCHAR(255))")

#insert data into the table
sql = "INSERT INTO students (name, address) VALUES (%s, %s)"
val = ("Jagriti", "Kathmandu")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

#read data from the table
mycursor.execute("SELECT * FROM students")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

#delete data from the table
sql = "DELETE FROM students WHERE address = 'lalitpur'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")