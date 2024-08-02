from sqlalchemy import Column,INTEGER,String
from database.connection import Base,CONNECTION

class Users(Base):
    __tablename__ = 'userdata'
    idx = Column(INTEGER,primary_key=True,autoincrement=True)
    name = Column(String(100))
    sname = Column(String(100))
# this creates a table if the table is not exists in the database
Base.meta_data.createall(CONNECTION)
