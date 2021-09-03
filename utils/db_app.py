from sqlalchemy import create_engine
from sqlalchemy.orm import Session,sessionmaker
from sqlalchemy import Boolean,Column,Integer,Float,String
from sqlalchemy.exc import SQLAlchemyError
from .config import DATABASE





# Now connect to the database created

#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
#SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://jojo89:Melody2Jason@localhost/Fastapi_test"

SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://jojo89:Melody2Jason@localhost:3306/{DATABASE}"
#SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://admin:Melody2Jason@database-1.csptufuwdfrf.us-west-2.rds.amazonaws.com:3306/fastapi_test"
engine = create_engine(SQLALCHEMY_DATABASE_URL,echo=True,)#connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def executeSQLCommand(sql_command: str,engine):
    try:
        engine.execute(sql_command)
        return True
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
    return False


