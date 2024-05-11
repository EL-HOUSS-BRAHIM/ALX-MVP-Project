import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="",  # Replace with your MySQL password
)

# Create a cursor object
cursor = conn.cursor()

# Create the database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS project_database")

# Switch to the created database
cursor.execute("USE project_database")

# Create users table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255) UNIQUE,
        hashed_password VARCHAR(255),
        country VARCHAR(255),
        currency VARCHAR(50),
        avatar VARCHAR(255),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
"""
)

# Create expenses table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS expenses (
        expense_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        amount DECIMAL(10, 2),
        category VARCHAR(255),
        currency VARCHAR(50),
        date DATE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
"""
)

# Create budgets table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS budgets (
        budget_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        category VARCHAR(255),
        amount DECIMAL(10, 2),
        currency VARCHAR(50),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
"""
)

# Create reminders table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS reminders (
        reminder_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        details TEXT,
        date DATE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
"""
)

# Optional: Create audit_logs table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS audit_logs (
        log_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        action VARCHAR(255),
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
"""
)

# Optional: Create user_settings table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS user_settings (
        settings_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        notification_preference BOOLEAN,
        display_preference VARCHAR(50),
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
"""
)

# Optional: Create notifications table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS notifications (
        notification_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        message TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
"""
)

# Optional: Create tags table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS tags (
        tag_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        name VARCHAR(255),
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
"""
)

# Optional: Create events table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS events (
        event_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        title VARCHAR(255),
        description TEXT,
        start_date DATE,
        end_date DATE,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
"""
)

# Commit changes and close connection
conn.commit()
conn.close()

print("Database schema created successfully.")
