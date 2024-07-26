from sqlalchemy import Column,INTEGER,String
from database.connection import Base

class Users(Base):
    __tablename__ = 'userdata'
    idx = Column(INTEGER,primary_key=True,autoincrement=True)
    name = Column(String(100))
    sname = Column(String(100))