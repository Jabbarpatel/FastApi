from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

CONNECTION_STRING = 'mysql://root:admin@localhost/user'
CONNECTION = create_engine(CONNECTION_STRING)
Session = sessionmaker(bind=CONNECTION)
session = Session()
Base = declarative_base()