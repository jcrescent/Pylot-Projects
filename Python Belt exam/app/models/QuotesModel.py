
from system.core.model import Model
import re

class QuotesModel(Model):
    def __init__(self):
        super(QuotesModel, self).__init__()
    
    def registration(self, user_data):
         
       
           ### Vaildation ### 
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        invalids = [] 

        if not user_data['name']:
            invalids.append("Name cannot be blank")
        elif len(user_data['name']) < 2:
            invalids.append("Name too short")
        if not user_data['alias']:
            invalids.append("Alias cannot be blank")    
        elif len(user_data['alias']) < 2:
            invalids.append("alias too short")
        if not user_data['email']:
            invalids.append("Email cannot be blank")
        elif not EMAIL_REGEX.match(user_data['email']):
            invalids.append("Please enter a valid email address")
        if not user_data['password']:
            invalids.append("password cannot be blank")    
        elif len(user_data['password']) < 8:
            invalids.append("Password must be at least 8 characters!")
        elif user_data['password'] != user_data['confirm']:
            invalids.append("Password and confirmation must match")
        if invalids:
            return {"status":False , "invalids":invalids}
        else:
            hashed_pw = self.bcrypt.generate_password_hash(user_data['password'])
            query = "INSERT INTO users (name, alias, email,  pw_hash, dob, created_at, updated_at) VALUES (:name, :alias, :email, :pw_hash, :dob,  NOW(), NOW())"
            data = {
                'name' : user_data['name'],
                'alias' : user_data['alias'],
                'email': user_data['email'], 
                'pw_hash' : hashed_pw,
                'dob' : user_data['dob']
                }
            
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
                return user[0]
        return False        

    def get_recent_quotes(self):
        query = "SELECT quotes.id AS id_quote, quotes.author, quotes.quote, quotes.creator_id, users.id, users.alias FROM quotes LEFT JOIN favorites ON quotes.id = favorites.quotes_id LEFT JOIN users ON users.id = favorites.users_id ORDER BY quotes.created_at DESC LIMIT 4"
        return self.db.query_db(query)

    def create_quote(self, quote_data):
        ###Validation###
        invalids = []
        if not quote_data['author']:
            invalids.append('Must enter person quoted')
        elif len(quote_data['author']) < 2:
            invalids.append('Name too short') 
        if not quote_data['quote']:
            invalids.append('Please enter a quote')
        if invalids:
            return {"status":False , "invalids":invalids}
        else:    
            query = 'INSERT INTO quotes(author, quote, creator_id, created_at, updated_at) VALUES (:author, :quote, :creator_id, NOW(), NOW())'    
            data = {
                'author': quote_data['author'],
                'quote' : quote_data['quote'],
                'creator_id' : quote_data['creator_id']
                }
            self.db.query_db(query,data)
        return {'status': True}

    def get_user_by_id(self, user_id):
        query="SELECT quotes.id AS id_quote, quotes.author, quotes.quote, quotes.creator_id, users.id AS id_user, users.alias FROM quotes LEFT JOIN favorites ON quotes.id = favorites.quotes_id LEFT JOIN users ON users.id = favorites.users_id WHERE quotes.creator_id = users.id ORDER BY quotes.created_at DESC"
        # data = {'id' : user_id}
        print self.db.query_db(query)
        return self.db.query_db(query)

    # def get_count(self, user_id) :

    # def add_to_favorites(self, favorites_data):
    #     query = "INSERT INTO favorites(quote_id AS idquotes, user_id AS iduser"

    # def get_favorites(self, user)
    #     query = 'INSERT INTO favorites(quote'           