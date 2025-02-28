import sqlite3
import csv

def init_db():
    conn = sqlite3.connect("library_inventory.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT,
                        author TEXT,
                        isbn TEXT UNIQUE,
                        quantity INTEGER,
                        location TEXT,
                        genre TEXT)''')
    conn.commit()
    conn.close()

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    isbn = input("Enter ISBN: ")
    quantity = input("Enter quantity: ")
    location = input("Enter shelf location (e.g., A5, 12, etc.): ")
    genre = input("Enter genre: ")

    if not title or not author or not isbn or not quantity or not location or not genre:
        print("Error: All fields are required!")
        return

    try:
        conn = sqlite3.connect("library_inventory.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author, isbn, quantity, location, genre) VALUES (?, ?, ?, ?, ?, ?)",
                       (title, author, isbn, int(quantity), location, genre))
        conn.commit()
        conn.close()
        print("Book added successfully!")
    except sqlite3.IntegrityError:
        print("Error: ISBN must be unique!")
    except Exception as e:
        print(f"Error: {e}")

def remove_book():
    isbn = input("Enter ISBN of the book to remove: ")
    try:
        conn = sqlite3.connect("library_inventory.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE isbn = ?", (isbn,))
        conn.commit()
        conn.close()
        print("Book removed successfully!")
    except Exception as e:
        print(f"Error: {e}")

def search_book():
    keyword = input("Enter book title or author to search: ")
    try:
        conn = sqlite3.connect("library_inventory.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", (f"%{keyword}%", f"%{keyword}%"))
        results = cursor.fetchall()
        conn.close()
        if results:
            for row in results:
                print(row)
        else:
            print("No books found!")
    except Exception as e:
        print(f"Error: {e}")

def import_books():
    file_path = input("Enter CSV file path: ")
    try:
        conn = sqlite3.connect("library_inventory.db")
        cursor = conn.cursor()
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header row
            for row in reader:
                cursor.execute("INSERT INTO books (title, author, isbn, quantity, location, genre) VALUES (?, ?, ?, ?, ?, ?)",
                               (row[0], row[1], row[2], int(row[3]), row[4], row[5]))
        conn.commit()
        conn.close()
        print("Books imported successfully!")
    except Exception as e:
        print(f"Error: {e}")

init_db()

while True:
    print("\nLibrary Inventory Management System")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Import Books from CSV")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        remove_book()
    elif choice == "3":
        search_book()
    elif choice == "4":
        import_books()
    elif choice == "5":
        break
    else:
        print("Invalid choice! Please try again.")

import sqlite3
import csv
from datetime import datetime

def init_db():
    conn = sqlite3.connect("library_inventory.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT,
                        author TEXT,
                        isbn TEXT UNIQUE,
                        quantity INTEGER,
                        location TEXT,
                        genre TEXT,
                        publisher TEXT,
                        date_added TEXT,
                        quantity_removed INTEGER,
                        date_removed TEXT)''')
    conn.commit()
    conn.close()

# Ensure the database is initialized before proceeding
init_db()

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    isbn = input("Enter ISBN: ")
    quantity = int(input("Enter quantity: "))
    location = input("Enter shelf location (e.g., A5, 12, etc.): ")
    genre = input("Enter genre: ")
    publisher = input("Enter publisher: ")
    date_added = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not title or not author or not isbn or not location or not genre or not publisher:
        print("Error: All fields are required!")
        return

    try:
        conn = sqlite3.connect("library_inventory.db")
        cursor = conn.cursor()
        cursor.execute("SELECT quantity FROM books WHERE isbn = ?", (isbn,))
        result = cursor.fetchone()

        if result:
            cursor.execute("UPDATE books SET quantity = quantity + ? WHERE isbn = ?", (quantity, isbn))
        else:
            cursor.execute("INSERT INTO books (title, author, isbn, quantity, location, genre, publisher, date_added) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                           (title, author, isbn, quantity, location, genre, publisher, date_added))

        conn.commit()
        conn.close()
        print("Book added successfully!")
    except Exception as e:
        print(f"Error: {e}")

def remove_book():
    isbn = input("Enter ISBN of the book to remove: ")
    quantity_to_remove = int(input("Enter quantity to remove: "))
    date_removed = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        conn = sqlite3.connect("library_inventory.db")
        cursor = conn.cursor()
        cursor.execute("SELECT quantity FROM books WHERE isbn = ?", (isbn,))
        result = cursor.fetchone()

        if result and result[0] >= quantity_to_remove:
            new_quantity = result[0] - quantity_to_remove
            if new_quantity > 0:
                cursor.execute("UPDATE books SET quantity = ?, quantity_removed = ?, date_removed = ? WHERE isbn = ?",
                               (new_quantity, quantity_to_remove, date_removed, isbn))
            else:
                cursor.execute("UPDATE books SET quantity_removed = ?, date_removed = ? WHERE isbn = ?",
                               (quantity_to_remove, date_removed, isbn))
                cursor.execute("DELETE FROM books WHERE isbn = ?", (isbn,))

            conn.commit()
            conn.close()
            print("Book removed successfully!")
        else:
            print("Error: Not enough books in stock or book not found!")
    except Exception as e:
        print(f"Error: {e}")

def search_book():
    keyword = input("Enter book title or author to search: ")
    try:
        conn = sqlite3.connect("library_inventory.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", (f"%{keyword}%", f"%{keyword}%"))
        results = cursor.fetchall()
        conn.close()
        if results:
            for row in results:
                print(row)
        else:
            print("No books found!")
    except Exception as e:
        print(f"Error: {e}")

def import_books():
    file_path = input("Enter CSV file path: ")
    try:
        conn = sqlite3.connect("library_inventory.db")
        cursor = conn.cursor()
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header row
            for row in reader:
                date_added = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                cursor.execute("INSERT INTO books (title, author, isbn, quantity, location, genre, publisher, date_added) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                               (row[0], row[1], row[2], int(row[3]), row[4], row[5], row[6], date_added))
        conn.commit()
        conn.close()
        print("Books imported successfully!")
    except Exception as e:
        print(f"Error: {e}")

while True:
    print("\nLibrary Inventory Management System")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Import Books from CSV")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        remove_book()
    elif choice == "3":
        search_book()
    elif choice == "4":
        import_books()
    elif choice == "5":
        break
    else:
        print("Invalid choice! Please try again.")


