
from system.core.model import Model
import re

class Book_reviewModel(Model):
    def __init__(self):
        super(Book_reviewModel, self).__init__()

    def register(self, user_data):
        hashed_pw = self.bcrypt.generate_password_hash(user_data['password']) 
        query = "INSERT INTO users (name, alias, email, pw_hash, created_at, updated_at) VALUES (:name, :alias, :email, :pw_hash,  NOW(), NOW())"
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

        def create_book_review(self, book_data, review_data):
            query = "INSERT INTO books(title, author, created_at, updated_at) VALUES (:title, :author, NOW(), NOW())"
            data = {
                'title': book_data['title'],
                'author': book_data['author']
            }
            self.db.query_db(query,data)

            get_book = "SELECT books.id FROM books ORDER BY books.created_at DESC LIMIT 1"
            book_id = get_book[0]

            query = "INSERT INTO reviews(review, rating, users_id, book_id) VALUES (:review, :rating, :user_id, NOW(), NOW())"
            data = {
                'review' : review_data['review'],
                'rating' : review_data['rating'],
                'user_id' : review_data['user-id'],
                'book_id': book_id
            }
            self.db.query_db(query, data) 

        def get_recent_reviews(self):
            query = "SELECT books.title, reviews.rating, users.alias, reviews.review, reviews.created_at FROM books JOIN reviews ON reviews.books_id = books.id  JOIN  users ON reviews.user_id = users.id ORDER BY reviews.created_at DESC LIMIT 3"
            return self.db.query_db(query)

        def get_all_reviews(self): 
            query = "SELECT books.title, book.id from books" 
            return self.db.query_db(query)

        def get_book_reviews(self, book_id):
            query = "SELECT books.title, reviews.rating, users.alias, reviews.review, reviews.created_at FROM books JOIN reviews ON reviews.books_id = books.id  JOIN  users ON reviews.user_id = users.id WHERE book.id = :id ORDER BY reviews.created_at DESC LIMIT 3 " 
            data = { 'id' : book_id }
            return self.db.query(query, data)
            
              