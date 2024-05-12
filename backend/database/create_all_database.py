#!/usr/bin/python3
import sys
import os

# Get the absolute path of the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to sys.path
sys.path.append(parent_dir)
# Convert sys.path to a set to remove duplicates, then convert it back to a list
unique_sys_path = list(set(sys.path))

# Print the unique entries in sys.path
for path in unique_sys_path:
    print(path)
import mysql.connector
from ..database.connection import get_connection

def create_database():
    """
    Create the 'project_database' database if it doesn't exist.
    """
    try:
        db_connection = get_connection()
        cursor = db_connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS project_database")
        print("Database created or already exists.")
    except mysql.connector.Error as error:
        print(f"Error creating database: {error}")
    finally:
        if db_connection.is_connected():
            cursor.close()
            db_connection.close()

def create_tables():
    """
    Create the necessary tables in the 'project_database' database.
    """
    try:
        db_connection = get_connection()
        cursor = db_connection.cursor()

        # Create users table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                email VARCHAR(255) NOT NULL UNIQUE,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
            )
            """
        )

        # Create expenses table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS expenses (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                category VARCHAR(255) NOT NULL,
                amount DECIMAL(10, 2) NOT NULL,
                description TEXT,
                date DATE NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
            """
        )

        # Create budgets table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS budgets (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                amount DECIMAL(10, 2) NOT NULL,
                category VARCHAR(255) NOT NULL,
                start_date DATE NOT NULL,
                end_date DATE NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
            """
        )

        # Create reminders table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS reminders (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                title VARCHAR(255) NOT NULL,
                description TEXT,
                due_date DATE NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
            """
        )

        print("Tables created or already exist.")
    except mysql.connector.Error as error:
        print(f"Error creating tables: {error}")
    finally:
        if db_connection.is_connected():
            cursor.close()
            db_connection.close()

if __name__ == "__main__":
    create_database()
    create_tables()
