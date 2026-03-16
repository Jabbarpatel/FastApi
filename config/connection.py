from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

CONNECTION_STRING = "mysql+pymysql://root:root@db:3306/test"
CONNECTION = create_engine(CONNECTION_STRING)
Session = sessionmaker(bind=CONNECTION)
session = Session()
BASE = declarative_base()
