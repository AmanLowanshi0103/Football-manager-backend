import pytest
from db import Base, engine, SessionLocal
from sqlalchemy.orm import Session

@pytest.fixture(scope="session", autouse=True)
def create_test_db():
    # Create tables
    Base.metadata.create_all(bind=engine)
    yield
    # Drop tables after test session
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def db_session():
    # Create a new session for a test
    session = SessionLocal()
    yield session
    session.close()
