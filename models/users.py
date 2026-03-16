from config.connection import BASE
from sqlalchemy import Column, String, INTEGER


class Users(BASE):
    __tablename__ = "users"

    id = Column(INTEGER, autoincrement=True, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
