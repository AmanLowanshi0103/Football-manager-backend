from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./test12.db"  # use in-memory SQLite for testing: sqlite:///:memory:

Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password=Column(String)

