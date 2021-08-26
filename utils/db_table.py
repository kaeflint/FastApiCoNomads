from sqlalchemy import Column,Integer,String,Boolean,Float
from sqlalchemy.orm import declarative_base
from .db_app import engine
Base = declarative_base()
Base.metadata.create_all(bind=engine)
class DBPlace(Base):
    __tablename__ = 'places'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    description = Column(String, nullable=True)
    coffee = Column(Boolean,)
    wifi = Column(Boolean)
    food = Column(Boolean)
    lat = Column(Float)
    lng = Column(Float)