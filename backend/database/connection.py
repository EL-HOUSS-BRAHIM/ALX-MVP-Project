from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# MySQL connection details
DB_HOST = "sql10.freemysqlhosting.net"  # Use the subdomain or the main domain where MySQL is accessible
DB_NAME = "sql10721737"
DB_USER = "sql10721737"
DB_PASS = "2ZaDJRTfjt"
PORT = 3306  # Default MySQL port is 3306

# Create SQLAlchemy engine with echo enabled
engine = create_engine(f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}:{PORT}/{DB_NAME}", echo=True)

# Create a session factory
Session = sessionmaker(bind=engine)

def get_session():
    return Session()

def test_connection():
    # Try to create a session and perform a simple query
    try:
        session = get_session()
        result = session.execute(text("SELECT 1"))
        for row in result:
            print(f"Test query result: {row}")
        session.close()
        print("Database connection successful and test query executed.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the test function
if __name__ == "__main__":
    test_connection()
