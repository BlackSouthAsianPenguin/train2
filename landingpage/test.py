import mysql.connector

try:
    connection = mysql.connector.connect(host='188.166.221.246',
                                        user='training',
                                         password='training')

    sql_select_Query = "select * from retail_db"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    print("\nPrinting each row")
    for row in records:
        print("Cattagories = ", row[0], )
        print("Customers = ", row[1])
        print("departments  = ", row[2])
        print("orders  = ", row[3], "\n")

except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("MySQL connection is closed")