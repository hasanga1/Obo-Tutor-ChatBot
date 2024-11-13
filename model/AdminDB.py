import os
from datetime import datetime, timezone
from sqlalchemy import create_engine, MetaData, Table, Column, String, DateTime, Integer

# Load environment variables
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DB = os.getenv("MYSQL_DB")

# Create SQLAlchemy engine
engine = create_engine(
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
)

# Define metadata
metadata = MetaData()

# Define tables
lecture_materials = Table(
    'lecture_materials',
    metadata,
    Column('id', Integer, primary_key=True),
    # Column('file', String(255)), 
    Column('file_name', String(255)),
    Column('file_type', String(255)),
    Column('uploaded_at', DateTime, default=lambda: datetime.now(timezone.utc))
)

# Connect to the database
connection = engine.connect()

# Create all tables in the database
metadata.create_all(engine)
