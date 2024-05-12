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

# MySQL connection details
DB_HOST = "sql5.freemysqlhosting.net"
DB_NAME = "sql5706017"
DB_USER = "sql5706017"
DB_PASS = "uCd4GTPbtR"
PORT = 3306

# Create a connection pool
db_pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="user_pool",
    pool_size=5,
    pool_reset_session=True,
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASS,
    database=DB_NAME,
    port=PORT
)

def get_connection():
    """
    Get a connection from the connection pool.
    """
    return db_pool.get_connection()