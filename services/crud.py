from sqlalchemy.orm import Session
from models.models import User
from schemas.schemas import UserCreate,LoginData
# import redis
from auth.auth import pwd_context,create_access_token



# # Connect to local Redis server
# r = redis.Redis(host='localhost', port=6379, db=0)

# if r is not None:
#     print("Redis connnected successfully",r)

def get_user(db: Session, user_id: int):
    # test=f"user:{user_id}"
    # cached_user=r.hgetall(test)
    # if cached_user:
    #     print("User from Redis")
    #     user_dict = {k.decode(): v.decode() for k, v in cached_user.items()}
    #     user_dict["id"] = user_id
    #     return user_dict 
    # else:
    #     print("User from the DB")

    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserCreate):
    print("Test 12", user)
    password=user.password
    hash_password=pwd_context.hash(password)
    db_user = User(name=user.name, email=user.email,password=hash_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    # if(db_user.id%2==0):
        # r.hset(f'user:{db_user.id}', mapping={'name': db_user.name, 'email': db_user.email})
    # data={"sub":db_user.email}
    # token=create_access_token(data)
    return db_user

def update_user(db:Session, user_id:int, user:UserCreate ):
    test=db.query(User).filter(User.id==user_id).first()
    if(test is None):
        return None
    test.name=user.name
    test.email=user.email
    db.add(test)
    db.commit()
    db.refresh(test)
    return test
    
def delete_user(db:Session, user_id:int):
    test=db.query(User).filter(User.id==user_id).first()
    if test is None:
        return None
    db.delete(test)
    db.commit()
    return test

def login_user(db:Session, user:LoginData):
    db_user=db.query(User).filter(User.email==user.email).first()
    if db_user is None :
        return None
    if pwd_context.verify(user.password,db_user.password):
        data={"sub":db_user.email}
        token=create_access_token(data)
        return token
    return None