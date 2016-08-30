# """ 
#     Sample Model File

#     A Model should be in charge of communicating with the Database. 
#     Define specific model method that query the database for information.
#     Then call upon these model method in your controller.

#     Create a model using this template.
# """
from system.core.model import Model
import re

class login_reg(Model):
    def __init__(self):
        super(login_reg, self).__init__()

    def register(self, user_data):
        hashed_pw = self.bcrypt.generate_password_hash(user_data['password']) 
        query = "INSERT INTO users (first_name, last_name, email,  pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash,  NOW(), NOW())"
        data = {
            'first_name' : user_data['first_name'],
            'last_name' : user_data['last_name'],
            'email': user_data['email'], 
            'pw_hash' : hashed_pw
            }
           ### Vaildation ### 
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        invalids = [] 
        if not user_data['first_name']:
            invalids.append("First name cannot be blank")
        elif len(user_data['first_name']) < 2:
            invalids.append("First name too short")
        if not user_data['last_name']:
            invalids.append("Last name cannot be blank")    
        elif len(user_data['last_name']) < 2:
            invalids.append("Last name too short")
        if not user_data['email']:
            invalids.append("Email cannot be blank")
        elif not EMAIL_REGEX.match(user_data['email']):
            invalids.append("please enter a valid email address")
        if not user_data['password']:
            invalids.append("password cannot be blank")    
        elif len(user_data['password']) < 8:
            invalids.append("Password must be at least 8 characters!")
        elif user_data['password'] != user_data['confirm']:
            invalids.append("Password and confirmation must match")
        if invalids:
            return {"status":False , "invalids":invalids}
        else:
            self.db.query_db(query,data)
            get_new_user = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            user = self.db.query_db(get_new_user)
            return {"status":True, "user":user[0]}

        

    def get_user(self, user_data):
        query = "SELECT * FROM users WHERE email = :email"
        data = {'email': user_data['email']}
        user = self.db.query_db(query,data)
        if user:
            if self.bcrypt.check_password_hash(user[0]['pw_hash'],user_data['password']):
                return user
        return False    
    # """
    # Below is an example of a model method that queries the database for all users in a fictitious application
    
    # Every model has access to the "self.db.query_db" method which allows you to interact with the database

    # def get_users(self):
    #     query = "SELECT * from users"
    #     return self.db.query_db(query)

    # def get_user(self):
    #     query = "SELECT * from users where id = :id"
    #     data = {'id': 1}
    #     return self.db.get_one(query, data)

    # def add_message(self):
    #     sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
    #     data = {'message': 'awesome bro', 'users_id': 1}
    #     self.db.query_db(sql, data)
    #     return True
    
    # def grab_messages(self):
    #     query = "SELECT * from messages where users_id = :user_id"
    #     data = {'user_id':1}
    #     return self.db.query_db(query, data)

    # """