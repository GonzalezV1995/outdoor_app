from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
mysqlconnection = "flaskposts"

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    def getALL():
        query = 'SELECT * FROM users;'
        connectToMySQL(mysqlconnection).query_db(query)

@classmethod 
def getAll(cls):
    query = '''
    SELECT *
    FROM users;'''
    things = connectToMySQL(mysqlconnection).query_db(query)
    pprint(things)
    output = []
    for stuff in things:
        output.append(cls(stuff))
    pprint(output)
    return output
