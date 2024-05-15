from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# MySQL connection details
DB_HOST = "sql5.freemysqlhosting.net"
DB_NAME = "sql5706017"
DB_USER = "sql5706017"
DB_PASS = "uCd4GTPbtR"
PORT = 3306

# Create SQLAlchemy engine
engine = create_engine(f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}:{PORT}/{DB_NAME}")

# Create a session factory
Session = sessionmaker(bind=engine)

def get_session():
    return Session()