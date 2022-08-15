import mysql.connector

#database connection
connection = mysql.connector(host="188.166.221.246",user="training",passwd="training",database="retail_db" )
cursor = connection.cursor()
# some other statements  with the help of cursor
connection.close()