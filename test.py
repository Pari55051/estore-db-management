import mysql.connector as ctor

try:
    dbcon = ctor.connect(host="localhost", user="root", password="0000", database="estore")

    if dbcon.is_connected:
        print("Connection established")
        cursor = dbcon.cursor()
        query="select * from complaints"
        cursor.execute(query)

        for rec in cursor.fetchall():
            print(rec)
        
except ctor.Error:
    print(ctor.Error)