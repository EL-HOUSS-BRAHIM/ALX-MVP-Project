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