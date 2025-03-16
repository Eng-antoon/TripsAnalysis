import sys
from sqlalchemy import create_engine
from config import DB_URI
from models import Base

def create_database():
    engine = create_engine(DB_URI)
    Base.metadata.create_all(engine)
    print("Database tables created successfully.")

if __name__ == "__main__":
    create_database()
    sys.exit(0)
