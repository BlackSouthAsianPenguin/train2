import pymysql

#database connection
connection = pymysql.connect(host="http://188.166.221.246/phpmyadmin",user="training",passwd="training",database="retail_db" )
cursor = connection.cursor()
# some other statements  with the help of cursor
connection.close()