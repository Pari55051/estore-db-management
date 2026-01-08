# all database-related functions
# connection and cursor are created in the main program


# ---------- ADD FUNCTIONS ---------- #

def add_inventory(cur, db):
    pid = int(input("Product ID: "))
    name = input("Product Name: ")
    qty = int(input("Quantity: "))
    price = float(input("Price: "))

    cur.execute(
        "INSERT INTO inventory VALUES (%s,%s,%s,%s)",
        (pid, name, qty, price)
    )
    db.commit()
    print("Product added successfully.")


def add_customer(cur, db):
    cid = int(input("Customer ID: "))
    name = input("Name: ")
    email = input("Email: ")
    addr = input("Address: ")
    bal = float(input("Unpaid Balance: "))

    cur.execute(
        "INSERT INTO customer VALUES (%s,%s,%s,%s,%s)",
        (cid, name, email, addr, bal)
    )
    db.commit()
    print("Customer added successfully.")


def add_transaction(cur, db):
    tid = int(input("Transaction ID: "))
    cid = int(input("Customer ID: "))
    mode = input("Payment Mode (Cash/Online): ")
    total = float(input("Total Amount: "))
    paid = float(input("Amount Paid: "))

    balance = total - paid

    cur.execute(
        "INSERT INTO transactions VALUES (%s,%s,%s,%s,%s,%s)",
        (tid, cid, mode, total, paid, balance)
    )
    db.commit()
    print("Transaction added successfully.")


def add_complaint(cur, db):
    comp_id = int(input("Complaint ID: "))
    cid = int(input("Customer ID: "))
    reason = input("Reason: ")
    status = input("Status (Pending/Resolved): ")

    cur.execute(
        "INSERT INTO complaints VALUES (%s,%s,%s,%s)",
        (comp_id, cid, reason, status)
    )
    db.commit()
    print("Complaint recorded.")


# ---------- READ FUNCTION ---------- #

def read_table(cur):
    print("\n--- Show Table Menu ---")
    print("1. Inventory")
    print("2. Customer")
    print("3. Transactions")
    print("4. Complaints")

    ch = input("Enter choice: ")

    if ch == "1":
        cur.execute("SELECT * FROM inventory")
    elif ch == "2":
        cur.execute("SELECT * FROM customer")
    elif ch == "3":
        cur.execute("SELECT * FROM transactions")
    elif ch == "4":
        cur.execute("SELECT * FROM complaints")
    else:
        print("Invalid choice.")
        return

    records = cur.fetchall()
    for row in records:
        print(row)


# ---------- DELETE FUNCTION ---------- #

def delete_record(cur, db):
    table = input("Enter table name: ")
    key_field = input("Enter primary key field name: ")
    key_value = int(input("Enter ID to delete: "))

    cur.execute(
        f"DELETE FROM {table} WHERE {key_field}=%s",
        (key_value,)
    )
    db.commit()
    print("Record deleted successfully.")


# ---------- MODIFY FUNCTIONS ---------- #

def update_inventory_quantity(cur, db):
    pid = int(input("Product ID: "))
    qty = int(input("New Quantity: "))

    cur.execute(
        "UPDATE inventory SET quantity=%s WHERE product_id=%s",
        (qty, pid)
    )
    db.commit()
    print("Inventory updated successfully.")


def update_payment_status(cur, db):
    tid = int(input("Enter Transaction ID: "))
    new_payment = float(input("Enter amount received: "))

    # Fetch current amount_paid and total_amount
    cur.execute("SELECT total_amount, amount_paid FROM transactions WHERE transaction_id=%s", (tid,))
    record = cur.fetchone()

    if record:
        total_amount, amount_paid = record
        amount_paid += new_payment
        balance = total_amount - amount_paid

        cur.execute(
            "UPDATE transactions SET amount_paid=%s, balance=%s WHERE transaction_id=%s",
            (amount_paid, balance, tid)
        )
        db.commit()
        print(f"Transaction updated. New Amount Paid: {amount_paid}, Balance: {balance}")
    else:
        print("Transaction not found.")


def update_complaint_status(cur, db):
    comp_id = int(input("Complaint ID: "))
    status = input("New Status: ")

    cur.execute(
        "UPDATE complaints SET status=%s WHERE complaint_id=%s",
        (status, comp_id)
    )
    db.commit()
    print("Complaint status updated.")


# ---------- ANALYSIS FUNCTIONS ---------- #

def product_availability(cur):
    name = input("Enter product name: ")

    cur.execute(
        "SELECT quantity FROM inventory WHERE product_name=%s",
        (name,)
    )
    result = cur.fetchone()

    if result:
        print("Quantity Available:", result[0])
    else:
        print("Product not found.")


def credit_sales(cur):
    cur.execute("""
        SELECT customer.customer_id,
               customer.name,
               transactions.transaction_id,
               transactions.balance
        FROM customer, transactions
        WHERE customer.customer_id = transactions.customer_id
        AND transactions.balance > 0
    """)

    records = cur.fetchall()

    if records:
        print("\nCustomers with Pending Dues:")
        for row in records:
            print("Customer ID:", row[0],
                  "| Name:", row[1],
                  "| Transaction ID:", row[2],
                  "| Pending Amount:", row[3])
    else:
        print("No credit sales found.")


def online_vs_cash(cur):
    cur.execute(
        "SELECT payment_mode, COUNT(*) FROM transactions GROUP BY payment_mode"
    )
    for row in cur.fetchall():
        print(row)


def complaint_feedback(cur):
    cur.execute(
        "SELECT reason, COUNT(*) FROM complaints GROUP BY reason"
    )
    for row in cur.fetchall():
        print(row)


def customer_total_dues(cur):
    cur.execute("""
        SELECT customer.customer_id, customer.name, SUM(transactions.balance) AS total_due
        FROM customer, transactions
        WHERE customer.customer_id = transactions.customer_id
        GROUP BY customer.customer_id
        HAVING total_due > 0
    """)
    records = cur.fetchall()
    if records:
        print("\nCustomers with Total Pending Dues:")
        for row in records:
            print(f"Customer ID: {row[0]}, Name: {row[1]}, Total Due: {row[2]}")
    else:
        print("No pending dues found.")


def low_stock_alert(cur):
    threshold = int(input("Enter stock threshold: "))
    cur.execute(
        "SELECT product_id, product_name, quantity FROM inventory WHERE quantity <= %s",
        (threshold,)
    )
    records = cur.fetchall()
    if records:
        print("\nLow Stock Items:")
        for row in records:
            print(f"Product ID: {row[0]}, Name: {row[1]}, Quantity: {row[2]}")
    else:
        print("No items below threshold.")


def pending_complaints(cur):
    cur.execute(
        "SELECT complaint_id, customer_id, reason FROM complaints WHERE status='Pending'"
    )
    records = cur.fetchall()
    if records:
        print("\nPending Complaints:")
        for row in records:
            print(f"Complaint ID: {row[0]}, Customer ID: {row[1]}, Reason: {row[2]}")
    else:
        print("No pending complaints found.")


def customer_purchase_history(cur):
    cid = int(input("Enter Customer ID: "))
    cur.execute("""
        SELECT transaction_id, total_amount, amount_paid, balance
        FROM transactions
        WHERE customer_id=%s
    """, (cid,))
    records = cur.fetchall()

    if records:
        print(f"\nTransaction history for Customer ID {cid}:")
        for row in records:
            print(f"Transaction ID: {row[0]}, Total: {row[1]}, Paid: {row[2]}, Balance: {row[3]}")
    else:
        print("No transactions found for this customer.")


def top_selling_products(cur):
    cur.execute("""
        SELECT inventory.product_id, inventory.product_name, COUNT(transactions.transaction_id) AS sold_count
        FROM inventory
        JOIN transactions ON inventory.product_id = transactions.transaction_id
        GROUP BY inventory.product_id, inventory.product_name
        ORDER BY sold_count DESC
        LIMIT 5
    """)
    records = cur.fetchall()

    if records:
        print("\nTop Selling Products:")
        for row in records:
            print(f"Product ID: {row[0]}, Name: {row[1]}, Sold Count: {row[2]}")
    else:
        print("No sales records found.")

def total_revenue(cur):
    cur.execute("SELECT SUM(amount_paid) FROM transactions")
    result = cur.fetchone()

    if result[0]:
        print(f"\nTotal Revenue Collected: {result[0]}")
    else:
        print("No revenue recorded yet.")

