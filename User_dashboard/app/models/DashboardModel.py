""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class DashboardModel(Model):
    def __init__(self):
        super(DashboardModel, self).__init__()

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

    def get_users(self):
        query = "SELECT * FROM users"
        return self.db.query_db(query)

    def get_user_by_id(self, user_id):
        query = "SELECT * FROM users WHERE id = :id"
        data = {'id': user_id}
        return self.db.query_db(query, data) 

    def get_user(self, user_data):
        query = "SELECT * FROM users WHERE email = :email"
        data = {'email': user_data['email']}
        user = self.db.query_db(query,data)
        if user:
            if self.bcrypt.check_password_hash(user[0]['pw_hash'], user_data['password']):
                return user
        return False 

    def add_message(self, message_info):
        query = "INSERT INTO messages(users_id, message, wall, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())"
        data = {
            'user_id': message_info['user_id'],
            'message': message_info['message'],
            'wall': message_info['wall']
        }

    def add_comment(self, ):
        query = "INSERT INTO comments(users_id, message, created_at, updated_at) VALUES (:"   
    def get_messages_by_id(self, user_id):
        query =  "SELECT * FROM messages JOIN users ON messages.users_id = users.id WHERE messages.wall = :id ORDER BY messages.created_at DESC"    
        data = {'id': user_id}
        return self.db.query_db(query, data)

    def get_comments_by_id(self, )    
        query = "SELECT * FROM comments JOIN users ON comments.users_id = users.id" 
        return self.db.query_db(query)

        

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