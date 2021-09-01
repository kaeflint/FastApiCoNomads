from sqlalchemy import create_engine
from sqlalchemy.orm import Session,sessionmaker
from sqlalchemy import Boolean,Column,Integer,Float,String

#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
#SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://jojo89:Melody2Jason@localhost/Fastapi_test"
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://jojo89:Melody2Jason@localhost:3306/Fastapi_test"
engine = create_engine(SQLALCHEMY_DATABASE_URL,echo=True,)#connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




