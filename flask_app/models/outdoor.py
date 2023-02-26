from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user


class Activity:
    db='outdoor_app_schema'
    def __init__(self,data):
        self.id = data['id']
        # self.name = data['name']
        self.location = data['location']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data ['updated_at']
        self.user=None

    @staticmethod
    def validate_activity(data):
        is_valid=True
        # if len(data.get('name'))<=3:    
        #     flash('Name needs at least 3 letters')
        #     is_valid=False
        if len(data.get('location'))<=3:  
            flash('Location needs at least 3 letters')  
            is_valid=False
        if len(data.get('description'))<=3:    
            flash('Descriptions need at least 3 letters')
            is_valid=False
            
            print(f'''
        name is: {data.get("name")}
        description is:{data.get("description")}
        ''')
        return is_valid

#Create


    @classmethod
    def get_all_activities(cls):
        query = "SELECT * FROM activities JOIN users ON users.id = activities.user_id;"
        activity_data = connectToMySQL ('outdoor_app_schema').query_db(query)
        print('A')
        all_activities=[]
        
        for activity_all in activity_data:

            activity_obj = cls(activity_all)
        
            activity_obj.user = user.User(
                {
                    "id":activity_all['user.id'],
                    "first_name":activity_all['first_name'],
                    "last_name":activity_all['last_name'],
                    "email":activity_all['email'],
                    "city":activity_all['city'],
                    "state":activity_all['state'],
                    "password": '',
                    "created_at":activity_all['user.created_at'],
                    "updated_at":activity_all['user.updated_at']
                }
            )
            all_activities.append(activity_obj)
        return all_activities  

    @classmethod
    def create_activity(cls,data):
        query ="""INSERT INTO activities (location, description, user_id) 
            VALUES (%(location)s, %(description)s, %(user_id)s);"""
        return (connectToMySQL(cls.db).query_db(query,data))

    @classmethod
    def update(cls,data):
        query = "UPDATE activities SET location=%(location)s, description=%(description)s, updated_at=NOW() WHERE id= %(id)s;"
        return connectToMySQL('outdoor_app_schema').query_db(query,data)

    @classmethod
    def get_activity_by_id(cls,data):
        
        query = "SELECT * FROM activities JOIN users ON users.id = activities.user_id WHERE activities.id = %(id)s;"
        result = connectToMySQL ('outdoor_app_schema').query_db(query,data)
        print('A')
        result = result[0]
        activity = cls(result) 
        
        activity.user = user.User(
            {
                "id":result['user.id'],
                "first_name":result['first_name'],
                "last_name":result['last_name'],
                "email":result['email'],
                "city":result['city'],
                "state":result['state'],
                "password": '',
                "created_at":result['user.created_at'],
                "updated_at":result['user.updated_at']
            }
        )

        return activity   

    @classmethod
    def delete(cls,id):
        data = {"id":id}
        query = "DELETE FROM activities WHERE id = %(id)s;"
        return connectToMySQL('outdoor_app_schema').query_db(query,data)