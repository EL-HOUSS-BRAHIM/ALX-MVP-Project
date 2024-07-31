#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import sys
import os

# Get the absolute path of the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Add the parent directory to sys.path
sys.path.append(parent_dir)
# Convert sys.path to a set to remove duplicates, then convert it back to a list
unique_sys_path = list(set(sys.path))

# Print the unique entries in sys.path
"""for path in unique_sys_path:
    print(path)"""

# Load environment variables from .env file
load_dotenv()

# Database connection details from .env file
DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASS')
}


def create_connection():
    """Create a database connection."""
    connection = None
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            print("Connection to MySQL DB successful")
    except Error as e:
        print(f"Error: {e}")
    return connection


def close_connection(connection):
    """Close the database connection."""
    if connection.is_connected():
        connection.close()
        print("Connection closed")


def create_user_table(connection):
    """Create the user table."""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS user (
        user_id INT PRIMARY KEY AUTO_INCREMENT,
        email VARCHAR(255) UNIQUE NOT NULL,
        hashed_password VARCHAR(255) NOT NULL,
        country VARCHAR(100),
        currency VARCHAR(10),
        balance DECIMAL(10, 2) DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        username VARCHAR(50) UNIQUE NOT NULL
    );
    """
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        connection.commit()
        print("User table created successfully")
    except Error as e:
        print(f"Error: {e}")


def create_token_table(connection):
    """Create the token table."""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS token (
        id INT PRIMARY KEY AUTO_INCREMENT,
        token VARCHAR(255) NOT NULL,
        expiry_date TIMESTAMP NOT NULL,
        user_id INT,
        FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE
    );
    """
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        connection.commit()
        print("Token table created successfully")
    except Error as e:
        print(f"Error: {e}")


def create_reminder_table(connection):
    """Create the reminder table."""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS reminder (
        id INT PRIMARY KEY AUTO_INCREMENT,
        details TEXT NOT NULL,
        user_id INT,
        date TIMESTAMP NOT NULL,
        FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE
    );
    """
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        connection.commit()
        print("Reminder table created successfully")
    except Error as e:
        print(f"Error: {e}")


def create_budget_table(connection):
    """Create the budget table."""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS budget (
        id INT PRIMARY KEY AUTO_INCREMENT,
        user_id INT,
        category VARCHAR(100) NOT NULL,
        amount DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE
    );
    """
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        connection.commit()
        print("Budget table created successfully")
    except Error as e:
        print(f"Error: {e}")


def create_transaction_table(connection):
    """Create the transaction table."""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS transaction (
        id INT PRIMARY KEY AUTO_INCREMENT,
        user_id INT,
        amount DECIMAL(10, 2) NOT NULL,
        category VARCHAR(100) NOT NULL,
        date TIMESTAMP NOT NULL,
        FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE
    );
    """
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        connection.commit()
        print("Transaction table created successfully")
    except Error as e:
        print(f"Error: {e}")


def create_status_table(connection):
    """Create the status table."""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS status (
        id INT PRIMARY KEY AUTO_INCREMENT,
        user_id INT UNIQUE NOT NULL,
        details TEXT NOT NULL,
        time TIMESTAMP NOT NULL,
        FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE
    );
    """
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        connection.commit()
        print("Status table created successfully")
    except Error as e:
        print(f"Error: {e}")


def create_action_table(connection):
    """Create the action table."""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS action (
        id INT PRIMARY KEY AUTO_INCREMENT,
        user_id INT,
        action_type VARCHAR(50) NOT NULL,
        details TEXT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE
    );
    """
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        connection.commit()
        print("Action table created successfully")
    except Error as e:
        print(f"Error: {e}")


def create_load_table(connection):
    """Create the load table."""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS load (
        id INT PRIMARY KEY AUTO_INCREMENT,
        user_id INT,
        details TEXT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE
    );
    """
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        connection.commit()
        print("Load table created successfully")
    except Error as e:
        print(f"Error: {e}")
