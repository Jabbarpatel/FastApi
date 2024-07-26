from database.connection import session
from models.models import Users

def get_all_user():
    return session.query(Users).all()

def get_users_by_page(page,page_size):
    return session.query(Users).limit(page_size).offset(int(page-1)*page_size).all()

def get_total_pages():
    return session.query(Users).count()

def get_user_by_filter(page,page_size,filter):
    return session.query(Users).filter(Users.name.like(f'%{filter}%')).limit(page_size).offset(int(page-1)*page_size).all()

def get_filtered_data_count(filter):
    return session.query(Users).filter(Users.name.like(f'%{filter}%')).count()

def get_user_by_idx(idx):
    return session.query(Users).filter(Users.idx == idx).first()

def delete_user_by_idx(idx):
    session.query(Users).delete(Users.idx==idx)
    session.commit()
    

