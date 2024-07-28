from dbqueries.access import DB_Queries
from execeptions import UserNotFoundExeception,UserAlreadyExistsExeception,UserIdxListNotFound
from models.models import Users
from database.connection import session


class DB():
    
    def get_user_data(page,page_size,filter):
        
        if page and page_size and filter:
            filtered_data = DB_Queries.get_user_by_filter(page,page_size,filter)
            if filtered_data:
                user_response_list = list()
                for data in filtered_data:
                    obj={
                        'idx':data.idx,
                        'fname':data.name,
                        'lname':data.sname
                    }
                    user_response_list.append(obj)
                    
            total_filtered_record_count = DB_Queries.get_filtered_data_count(filter)
        
            total_pages = int(total_filtered_record_count) / int(page_size)
                
            if int(total_filtered_record_count) % int(page_size) != 0:
                total_pages += 1
                
            return {
                    'user_list':user_response_list,
                    'total_pages':int(total_pages)
                }
            
        elif page and page_size:
            user_list = DB_Queries.get_users_by_page(page,page_size)
            if user_list:
                user_response_list= list()
                for data in user_list:
                    obj={
                        'idx':data.idx,
                        'fname':data.name,
                        'lname':data.sname
                    }
                    user_response_list.append(obj)
            
            total_records = DB_Queries.get_total_pages()
            if total_records:
                total_pages = int(total_records) / int(page_size)
                
                if int(total_records) % int(page_size) != 0:
                    total_pages += 1
                    
            return {
                    'user_list':user_response_list,
                    'total_pages':int(total_pages)
                }
            
        else:
            user_list = DB_Queries.get_all_user()
            if user_list:
                user_response_list = list()
                for data in user_list:
                    obj = {
                        'idx':data.idx,
                        'fname':data.name,
                        'lname':data.sname
                    }
                    user_response_list.append(obj)
            return user_response_list
            
                    
    def delete_user(idx):
        user_exits = DB_Queries.get_user_by_idx(idx)
        
        if user_exits:
            session.delete(user_exits)
            session.commit()
            
        else:
            raise UserNotFoundExeception(idx)
        
    def add_user(idx,first_name,last_name):
        
        if idx:
            idx_exists = DB_Queries.get_user_by_idx(idx)
            if idx_exists:
                raise UserAlreadyExistsExeception(idx)
            else:
                new_user = Users(idx = idx,name = first_name,sname = last_name)
                session.add(new_user)
                session.commit()
                
        else:
            all_user_idx = [item.idx for item in DB_Queries.get_all_idx_of_users()]
            
            if all_user_idx:
                max_id = max(all_user_idx)
                min_id = min(all_user_idx)

                avaialble_idx = set(range(min_id,max_id+1))-set(all_user_idx)

                if len(list(avaialble_idx)) > 0:
                    new_user = Users(idx = list(avaialble_idx)[0],name = first_name,sname = last_name)
                    session.add(new_user)
                    session.commit()
                    
                else:
                    new_user = Users(name = first_name,sname = last_name)
                    session.add(new_user)
                    session.commit()
                    
            else:
                raise UserIdxListNotFound
    
    def update_user(idx,first_name,last_name):
        
        user_exists = DB_Queries.get_user_by_idx(idx)
        if user_exists:
            user_exists.name = first_name
            user_exists.sname = last_name
            session.commit()
            
        else:
            raise UserNotFoundExeception(idx)
                
        
