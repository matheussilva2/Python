import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passw="root")

mycursor = mydb.cursor() //