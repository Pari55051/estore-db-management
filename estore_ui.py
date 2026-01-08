import mysql.connector
import estore_functions as ef


# ---------- MySQL CONNECTION ----------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0000",
    database="estore"
)

cur = db.cursor()


# ---------- OPERATION FUNCTIONS ----------

def add_operation():
    print("\n--- Add Menu ---")
    print("1. Add Inventory")
    print("2. Add Customer")
    print("3. Add Transaction")
    print("4. Add Complaint")

    ch = input("Enter choice: ")

    if ch == "1":
        ef.add_inventory(cur, db)
    elif ch == "2":
        ef.add_customer(cur, db)
    elif ch == "3":
        ef.add_transaction(cur, db)
    elif ch == "4":
        ef.add_complaint(cur, db)
    else:
        print("Invalid choice.")


def delete_operation():
    ef.delete_record(cur, db)


def modify_operation():
    print("\n--- Modify Menu ---")
    print("1. Update Inventory Quantity")
    print("2. Update Complaint Status")
    print("3. Update Payment Status")

    ch = input("Enter choice: ")

    if ch == "1":
        ef.update_inventory_quantity(cur, db)
    elif ch == "2":
        ef.update_complaint_status(cur, db)
    elif ch == "3":
        ef.update_payment_status(cur, db)
    else:
        print("Invalid choice.")


def read_operation():
    ef.read_table(cur)


def analysis_operation():
    while True:
        print("\n--- Analysis Menu ---")
        print("1. Product Availability")
        print("2. Credit Sales")
        print("3. Online vs Cash Transactions")
        print("4. Complaint Feedback")
        print("5. Customer Total Dues")
        print("6. Low Stock Alert")
        print("7. Pending Complaints")
        print("8. Customer Purchase History")
        print("9. Top Selling Products")
        print("10. Total Revenue")
        print("11. Back to Main Menu")

        ch = input("Enter choice: ")

        if ch == "1":
            ef.product_availability(cur)
        elif ch == "2":
            ef.credit_sales(cur)
        elif ch == "3":
            ef.online_vs_cash(cur)
        elif ch == "4":
            ef.complaint_feedback(cur)
        elif ch == "5":
            ef.customer_total_dues(cur)
        elif ch == "6":
            ef.low_stock_alert(cur)
        elif ch == "7":
            ef.pending_complaints(cur)
        elif ch == "8":
            ef.customer_purchase_history(cur)
        elif ch == "9":
            ef.top_selling_products(cur)
        elif ch == "10":
            ef.total_revenue(cur)
        elif ch == "11":
            break
        else:
            print("Invalid choice. Please try again.")



# ---------- MAIN PROGRAM LOOP ----------
while True:
    print("\n===== E-STORE MANAGEMENT SYSTEM =====")
    print("1. Add Record")
    print("2. Delete Record")
    print("3. Modify Record")
    print("4. Read Records")
    print("5. Analysis")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_operation()

    elif choice == "2":
        delete_operation()

    elif choice == "3":
        modify_operation()

    elif choice == "4":
        read_operation()

    elif choice == "5":
        analysis_operation()

    elif choice == "6":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")


# ---------- CLOSE CONNECTION ----------
cur.close()
db.close()