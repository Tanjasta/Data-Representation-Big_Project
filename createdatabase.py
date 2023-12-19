import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  
  database="car"
)

cursor = db.cursor()
sql="CREATE TABLE car (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(250),model VARCHAR(250), pice INT)"

cursor.execute(sql)

db.close()
cursor.close()