from dbqueries.access import get_all_user,get_users_by_page,get_total_pages,get_user_by_filter,get_filtered_data_count,get_user_by_idx,delete_user_by_idx
from execeptions import DeleteUserExeception,UserAlreadyExistsExeception


class DB():
    
    def get_user_data(page,page_size,filter):
        
        if page and page_size and filter:
            filtered_data = get_user_by_filter(page,page_size,filter)
            if filtered_data:
                user_response_list = list()
                for data in filtered_data:
                    obj={
                        'idx':data.idx,
                        'fname':data.name,
                        'lname':data.sname
                    }
                    user_response_list.append(obj)
                    
            total_filtered_record_count = get_filtered_data_count(filter)
        
            total_pages = int(total_filtered_record_count) / int(page_size)
                
            if int(total_filtered_record_count) % int(page_size) != 0:
                total_pages += 1
                
            return {
                    'user_list':user_response_list,
                    'total_pages':int(total_pages)
                }
            
        elif page and page_size:
            user_list = get_users_by_page(page,page_size)
            if user_list:
                user_response_list= list()
                for data in user_list:
                    obj={
                        'idx':data.idx,
                        'fname':data.name,
                        'lname':data.sname
                    }
                    user_response_list.append(obj)
            
            total_records = get_total_pages()
            if total_records:
                total_pages = int(total_records) / int(page_size)
                
                if int(total_records) % int(page_size) != 0:
                    total_pages += 1
                    
            return {
                    'user_list':user_response_list,
                    'total_pages':int(total_pages)
                }
            
        else:
            user_list = get_all_user()
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
        user_exits = get_user_by_idx(idx)
        if user_exits:
            delete_user_by_idx(idx)
        else:
            raise DeleteUserExeception(idx)
        
    def add_user(idx,first_name,last_name):
        idx_exists = get_user_by_idx(idx)
        if idx_exists:
            raise UserAlreadyExistsExeception(idx)
        else:
            pass
            
        