from sqlalchemy import create_engine
from sqlalchemy.orm import Session,declarative_base,sessionmaker
from sqlalchemy import Boolean,Column,Integer,Float,String

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL,echo=True,connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




