# estore.py

### IMPORTS ###
import mysql.connector as mysql
import project.archive.menu as menu

### __MAIN__ ###
dbcon = mysql.connect(host="localhost", user="root", passwd="0000", database="estore")
cursor = dbcon.cursor()

while True:  # repeated input until otherwise instructed
    # Operations Menu
    print("\nOptions menu:")
    print("1. Add new data into desired table.")
    print("2. Delete records from desired table.")
    print("3. Change records in desired table.")
    print("4. Display data of desired table.")
    print("5. check availabilit of product")
    print("6. Display records corresponding to credit sales.")
    print("7. Display no. of transactions of each type, cash and online.")
    print("8. Display no. of complaints for each type.")
    print("9. Exit\n")

    ch = int(input("Enter your choice:"))

    if ch == 1:  # Add new data into desired table
        table = input("Enter the name of table:")

        values = eval(input("Enter the values in the form of tuple:"))

        menu.insertinto(table, values)
        # print("Done")
    
    elif ch == 2:  # Delete records from desired table
        table = input("Enter the name of table:")
        condition = input("Enter the condition:")

        menu.delete(table, condition)
        # print("Deleted")
    
    elif ch == 3:  # Change records in desired table
        table = input("Enter the name of table:")
        update_data = input("Enter the data to be updated:")
        condition = input("Enter condition:")

        menu.update(table, update_data, condition)
        # print("Record updated.")
    
    elif ch == 4:  # Display data of desired table
        table = input("Enter the name of table:")

        menu.readall(table)
    
    elif ch == 5:  # Check availability of product
        product_id = int(input("Enter product ID:"))

        menu.available(product_id)
    
    elif ch == 6:  # Display records corresponding to credit sales
        menu.credit()
    
    elif ch == 7:  # Display no. of transaction of each type, cash and online
        menu.cashcredit()
    
    elif ch == 8:  # Display no. of complaints for each type
        menu.complaint()
    
    elif ch == 9:  # exit
        print("Exit...")
        break

    else:
        print("Invalid choice.")

dbcon.close()
