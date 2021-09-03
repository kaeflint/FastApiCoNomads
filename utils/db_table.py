from typing import Text
from sqlalchemy import Column,Integer,String,Boolean,Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.expression import null
from .db_app import engine
Base = declarative_base()
Base.metadata.create_all(bind=engine)
class DBPlace(Base):
    __tablename__ = 'places'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(50))
    description = Column(String, nullable=True)
    coffee = Column(Boolean,)
    wifi = Column(Boolean)
    food = Column(Boolean)
    lat = Column(Float)
    lng = Column(Float)

class DBUsers(Base):
    __tablename__='tb_users'
    id = Column(Integer, primary_key=True, autoincrement=True,index=True)
    username= Column(String,nullable=False)
    pswd= Column(Text,nullable=True)