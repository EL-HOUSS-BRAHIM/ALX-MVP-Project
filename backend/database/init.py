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
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# MySQL connection details
DB_HOST = "phpadmin.brahim-crafts.tech"
DB_NAME = "project"
DB_USER = "bross"
DB_PASS = "A78BE9D10s?"
PORT = 3306
DB_URI = f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}:{PORT}/{DB_NAME}"

# Create a database engine
engine = create_engine(DB_URI)

# Create a thread-safe session factory
Session = scoped_session(sessionmaker(bind=engine))

# Create a declarative base for defining database models
Base = declarative_base()

def create_tables():
    """
    Create all the tables in the database.
    """
    from database.models import Base
    Base.metadata.create_all(engine)
    print("Tables created successfully.")

def drop_tables():
    """
    Drop all the tables from the database.
    """
    from database.models import Base
    Base.metadata.drop_all(engine)
    print("Tables dropped successfully.")
