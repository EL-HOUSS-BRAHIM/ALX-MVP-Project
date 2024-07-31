#!/usr/bin/python3
from create_table import create_connection, close_connection, create_user_table

def test_create_user_table():
    """Test the creation of the user table."""
    connection = create_connection()
    if connection:
        create_user_table(connection)
        close_connection(connection)

if __name__ == "__main__":
    test_create_user_table()