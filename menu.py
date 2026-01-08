# MENU FUNCTIONS

def insertinto(table, val):
    ''' parameters: table (str), val (eval)
        return: None
    '''

    st = "INSERT INTO" + table + "VALUES(" + val + ")"
    
    cursor.execute(st)
    dbcon.commit()

    print("Added!")


def delete(table, condition):
    ''' parameters: table (str), condition (eval)
        return: None
    '''

    st = "DELETE FROM" + table + "WHERE" + condition

    cursor.execute(st)
    dbcon.commit()

    print("Deleted!")


def update(table, update_data, condition):
    ''' parameters: table (str), update_data (str), condition (str)
        return: None
    '''

    st = "UPDATE" + table + "SET" + update_data + "WHERE" + condition

    cursor.excute(st)
    dbcon.commit()

    print("Updated!")


def readall(table):
    ''' parameters: table (str)
        return: None
    '''

    st = "SELECT * FROM" + table

    cursor.execute(st)

    for rec in cursor.fetchall():
        print(rec)


def available(product_id):
    ''' parameters: product (int)
        return: None
    '''

    cursor.execute("SELECT * FROM inventory WHERE PID = {}".format(product_id))
    data = cursor.fetchall()

    found = False

    for rec in data:
        if rec[0] == product_id:
            found = True
            qty = rec[2]
            break

    if found:
        print("Item found. The no of items available:", qty)
    else:
        print("Item not available.")


def credit():
    ''' parameters: None
        return: None
    '''

    cursor.execute("SELECT * FROM transaction")
    data = cursor.fetchall()

    print("The following records are for credit sales:")
    for rec in data:
        if rec[4] != 0:
            print(rec)


def cashcredit():
    ''' parameters: None
        return: None
    '''

    cursor.execute("SELECT DISTINCT co, COUNT(*) FROM transaction GROUP BY co")
    data = cursor.fetchall()

    print("Following are the no. of transactions of each type:")
    for rec in data:
        print(rec)


def complaint():
    ''' parameters: None
        return: None
    '''
    cursor.execute("SELECT DISTINCT CptReason, COUNT(*) FROM complaints GROUP BY CptReason")
    data = cursor.fetchall()

    print("Following are the no. of complaints of each type:")
    for rec in data:
        print(rec)


# __MAIN__

import mysql.connector as mysql

dbcon = mysql.connect(host="localhost", user="root", passwd="0000", database="estore")
cursor = dbcon.cursor()
