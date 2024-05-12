import mysql.connector

# MySQL connection details
HOST = "sql5.freemysqlhosting.net"
DATABASE = "sql5706017"
USER = "sql5706017"
PASSWORD = "uCd4GTPbtR"
PORT = 3306

# Create a connection pool
connection_pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="expense_tracker_pool",
    pool_size=5,
    pool_reset_session=True,
    host=HOST,
    database=DATABASE,
    user=USER,
    password=PASSWORD,
    port=PORT
)

def get_connection():
    """
    Get a connection from the connection pool.

    Returns:
        MySQLConnection: A connection object from the pool.
    """
    return connection_pool.get_connection()