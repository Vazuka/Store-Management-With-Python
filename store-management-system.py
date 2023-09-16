import pandas as pd
import pymysql
import hashlib  # For password hashing
import getpass  # For securely inputting passwords
import datetime
import matplotlib.pyplot as plt
import numpy as np

# Initialize database connection and cursor
def initialize_db():
    conn = pymysql.connect(host='localhost', user='root', password='enter-your-mysql-password-here')
    cursor = conn.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS store_management')
    cursor.execute('USE store_management')
    return conn, cursor

# Create tables if they don't exist
def create_tables(cursor):
    cursor.execute('CREATE TABLE IF NOT EXISTS Admin(Username VARCHAR(20) PRIMARY KEY, Password VARCHAR(64))')
    cursor.execute('CREATE TABLE IF NOT EXISTS Billing_System(Sl_No INT PRIMARY KEY, Product_Name VARCHAR(30), Price FLOAT(9,2), Discount INT, GST FLOAT(5,2))')

# Hash passwords for storage in the database
def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    password_hash = binascii.hexlify(password_hash)
    return (salt + password_hash).decode('ascii')

# Verify a user's password
def verify_password(stored_password, provided_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    password_hash = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt.encode('ascii'), 100000)
    password_hash = binascii.hexlify(password_hash).decode('ascii')
    return password_hash == stored_password

# Main menu
def main_menu(conn, cursor):
    while True:
        print('******************************!!WELCOME!!******************************')
        print('1. Existing Admin')
        print('2. New Admin')
        print('3. Exit')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            login(conn, cursor)
        elif choice == 2:
            create_admin(conn, cursor)
        elif choice == 3:
            conn.close()
            exit()
        else:
            print('INVALID CHOICE!!')

# Admin login
def login(conn, cursor):
    user = input('Enter your username: ')
    password = getpass.getpass('Enter your password: ')
    
    cursor.execute("SELECT Password FROM Admin WHERE Username=%s", (user,))
    stored_password = cursor.fetchone()
    
    if stored_password and verify_password(stored_password[0], password):
        print('Login successful.')
        admin_menu(conn, cursor)
    else:
        print('Invalid username or password.')

# Admin menu
def admin_menu(conn, cursor):
    while True:
        print('1. Add Product')
        print('2. Search for Product')
        print('3. Update Product details')
        print('4. Delete Product')
        print('5. Sales Status')
        print('6. View Table')
        print('7. Log Out')
        choice = int(input('Enter your Choice: '))
        if choice == 1:
            add_product(conn, cursor)
        elif choice == 2:
            search_product(conn, cursor)
        # Implement other admin menu options...
        elif choice == 7:
            print('Logging out...')
            return
        else:
            print('INVALID CHOICE!!')

# Add a product
def add_product(conn, cursor):
    print("Add a New Product")
    sl_no = input('Enter Sl_No: ')
    product_name = input('Enter Product_Name: ')
    price = float(input('Enter Price: '))
    discount = int(input('Enter Discount(%): '))
    gst = float(input('Enter GST(%): '))
    
    # Insert the product into the Billing_System table
    try:
        cursor.execute("INSERT INTO Billing_System (Sl_No, Product_Name, Price, Discount, GST) VALUES (%s, %s, %s, %s, %s)",
                       (sl_no, product_name, price, discount, gst))
        conn.commit()
        print('PRODUCT ADDED SUCCESSFULLY!!')
    except pymysql.Error as e:
        conn.rollback()
        print(f"Error adding the product: {e}")

# Search for a product
def search_product(conn, cursor):
    sl_no = input('Enter Sl_No: ')
    cursor.execute('SELECT * FROM Billing_System WHERE Sl_No = %s', (sl_no,))
    data = cursor.fetchone()
    
    if data is None:
        print('PRODUCT NOT FOUND!!')
    else:
        print('PRODUCT FOUND')
        print('Product_Name=', data[1])
        print('Price=', data[2])
        print('Discount=', data[3])
        print('GST=', data[4])

# Create a new admin account
def create_admin(conn, cursor):
    print("Creating a New Admin Account")
    user = input('Enter New Username: ')
    password = getpass.getpass('Enter New Password: ')
    
    # Hash the password before storing it in the database
    hashed_password = hash_password(password)
    
    try:
        cursor.execute("INSERT INTO Admin (Username, Password) VALUES (%s, %s)", (user, hashed_password))
        conn.commit()
        print('!! NEW ADMIN ADDED SUCCESSFULLY !!')
    except pymysql.Error as e:
        conn.rollback()
        print(f"Error creating admin: {e}")

# Data visualization
def visualize_data(conn, cursor):
    while True:
        print('1. Yearly Basis')
        print('2. Monthly Basis')
        print('3. Back to Admin Menu')
        choice = int(input('Enter your choice: '))
        
        if choice == 1:
            cursor.execute("SELECT Year, SUM(Profit) FROM YearlySales GROUP BY Year")
            yearly_data = cursor.fetchall()
            if not yearly_data:
                print("Insufficient data for yearly visualization.")
            else:
                years, profits = zip(*yearly_data)
                plt.plot(years, profits, marker='D', markeredgecolor='maroon')
                plt.ylabel('Total Profit (In Lakh Rs.)')
                plt.xlabel('Year')
                plt.title('YEARLY PROFIT')
                plt.show()
        elif choice == 2:
            cursor.execute("SELECT Month, SUM(Profit) FROM MonthlySales WHERE Year = YEAR(CURDATE()) GROUP BY Month")
            monthly_data = cursor.fetchall()
            if not monthly_data:
                print("Insufficient data for monthly visualization for the current year.")
            else:
                months, monthly_profits = zip(*monthly_data)
                plt.plot(months, monthly_profits, marker='D', markeredgecolor='maroon')
                plt.ylabel('Total Profit (In Rs.)')
                plt.xlabel('Month')
                plt.title('MONTHLY PROFIT (Current Year)')
                plt.show()
        elif choice == 3:
            break
        else:
            print('INVALID CHOICE!!')

if __name__ == "__main__":
    conn, cursor = initialize_db()
    create_tables(cursor)
    main_menu(conn, cursor)
