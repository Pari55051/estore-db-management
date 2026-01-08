# E-Store Management System

## Synopsis

### Introduction

A local convenience store wants to start its online business. They require a **database management system** to efficiently manage inventory, transactions, customer information, and complaints.

This project automates the following:

1. **Inventory Tracking**

   * Keeps the store’s website up-to-date with the actual availability of items.
   * Saves the manual effort of updating product quantities for every change.

2. **Transaction Management**

   * Organizes sales data and payments.
   * Helps prepare accounts and track pending payments efficiently.

3. **Customer Information Management**

   * Maintains customer details such as name and contact info.
   * Speeds up order processing and delivery.

4. **Complaint Management**

   * Records customer complaints and their status.
   * Helps identify recurring problems and improve customer satisfaction.

**Technologies used:** Python 3.12, MySQL

---

## Basic Information

### Python Programs Used

1. **estore_functions.py**

   * Contains all the **functions** for add, delete, modify, read, and analysis operations.
   * Functions are modular and can be called from the user interface.

2. **estore_ui.py**

   * Main program with a **menu-driven interface**.
   * Uses the functions in `estore_functions.py` to perform operations.
   * Establishes the **database connection** and manages the menu loop.

---

### Database and Tables

**Database:** `estore`
**Tables included:**

#### 1. Inventory Table

* **Purpose:** Stores information about products available in the store.

* **Fields:**

  * `product_id` (INTEGER, PRIMARY KEY) – Unique product identifier
  * `product_name` (VARCHAR, NOT NULL) – Name of the product
  * `quantity` (INTEGER, NOT NULL) – Available stock
  * `price` (DECIMAL, NOT NULL) – Price per unit

* **Usage:**

  * Adding new products
  * Updating quantity or price
  * Checking stock availability
  * Generating low stock alerts

---

#### 2. Customer Table

* **Purpose:** Stores customer information.

* **Fields:**

  * `customer_id` (INTEGER, PRIMARY KEY) – Unique customer identifier
  * `name` (VARCHAR, NOT NULL) – Customer name
  * `email` (VARCHAR, UNIQUE) – Optional, for record keeping
  * `address` (VARCHAR) – Optional, delivery address

* **Usage:**

  * Recording customer information
  * Linking with transactions and complaints
  * Analysis of customer purchase history and total dues

---

#### 3. Transactions Table

* **Purpose:** Tracks sales transactions.

* **Fields:**

  * `transaction_id` (INTEGER, PRIMARY KEY) – Unique transaction ID
  * `customer_id` (INTEGER, FOREIGN KEY → Customer.customer_id) – Customer who made the purchase
  * `payment_mode` (VARCHAR) – Cash or Online
  * `total_amount` (DECIMAL) – Total bill amount
  * `amount_paid` (DECIMAL) – Amount received from the customer
  * `balance` (DECIMAL) – Pending amount

* **Usage:**

  * Recording sales
  * Tracking payments and pending balances (credit sales)
  * Generating total revenue and payment-mode analysis

---

#### 4. Complaints Table

* **Purpose:** Records customer complaints.

* **Fields:**

  * `complaint_id` (INTEGER, PRIMARY KEY) – Unique complaint identifier
  * `customer_id` (INTEGER, FOREIGN KEY → Customer.customer_id) – Customer who lodged the complaint
  * `reason` (VARCHAR) – Complaint reason
  * `status` (VARCHAR) – Pending / Resolved

* **Usage:**

  * Logging complaints
  * Tracking complaint resolution
  * Generating feedback analysis and pending complaints list

---

### Relationships Between Tables

| Parent Table | Child Table  | Relationship                                               |
| ------------ | ------------ | ---------------------------------------------------------- |
| Customer     | Transactions | One-to-many (one customer can have multiple transactions)  |
| Customer     | Complaints   | One-to-many (one customer can lodge multiple complaints)   |
| Transactions | Inventory    | Indirect (transaction records correspond to products sold) |

* All functions in Python **use `customer_id` as the linking key**.
* Balance for credit sales is always derived from `transactions.balance`.

---

## Input and Output

### Input

* Initial input: populate tables with products, customers, transactions, complaints.
* Ongoing input: add, modify, or delete records using the menu options.

### Output

* Display tables and records using menu options.
* Generate analysis reports:

  * Product availability
  * Credit sales per customer
  * Online vs cash transactions
  * Complaint feedback and pending complaints
  * Customer total dues
  * Low stock alert
  * Customer purchase history
  * Top selling products
  * Total revenue

---

## Menu Options and Functions

### 1. **Add Records**

* Add inventory, customers, transactions, or complaints.
* Updates corresponding tables in MySQL.

### 2. **Delete Records**

* Delete records from any table based on ID.

### 3. **Modify Records**

* Update inventory quantity or complaint status.
* Update payment status in transactions to reflect new payments.

### 4. **Show Table**

* Displays selected table (Inventory, Customer, Transactions, Complaints) in the console.

### 5. **Analysis / Reports**

1. **Product Availability:** Checks stock quantity of a specific product.
2. **Credit Sales:** Lists transactions with pending balance along with customer details.
3. **Online vs Cash Transactions:** Counts number of transactions for each payment mode.
4. **Complaint Feedback:** Shows number of complaints for each reason.
5. **Customer Total Dues:** Displays total pending amount per customer.
6. **Low Stock Alert:** Displays items below a specified threshold quantity.
7. **Pending Complaints:** Lists all complaints not yet resolved.
8. **Customer Purchase History:** Shows all transactions for a specific customer.
9. **Top Selling Products:** Displays most frequently sold products.
10. **Total Revenue:** Displays total amount collected from all transactions.

---

## Program Flow

1. Establish connection to MySQL database.
2. Display **main menu** in console.
3. User selects operation: **Add / Delete / Modify / Read / Analysis / Exit**.
4. Submenus and functions guide the user through **all operations**.
5. On exit, database connection is closed.

---
