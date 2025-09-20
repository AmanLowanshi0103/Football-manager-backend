import pytest
from conftest import db_session, create_test_db
from db import User
from services.crud import create_user, get_user, update_user,delete_user


# create_test_db()

user=User(name="test",email="test@gmail.com",password="test")

def test_createuser(db_session):
    test_curd=create_user(db_session,user)
    print(test_curd)
    assert test_curd.email==user.email

def test_getUser(db_session):
    test_curd=get_user(db_session,1)
    assert test_curd.email==user.email


def test_deleteuser(db_session):
    test_curd=get_user(db_session,1)
    assert test_curd.email==user.email

