# """ 
#     Sample Model File

#     A Model should be in charge of communicating with the Database. 
#     Define specific model method that query the database for information.
#     Then call upon these model method in your controller.

#     Create a model using this template.
# """
from system.core.model import Model

class productsModel(Model):
    def __init__(self):
        super(productsModel, self).__init__()

    def add_product(self, product_data):
        query = "INSERT INTO products (name, description, price, created_at, updated_at) VALUES (:name, :description, :price, NOW(), NOW())" 
        data = {
            'name' : product_data['name'],
            'description' : product_data['description'],
            'price' : product_data['price']
        }
        return self.db.query_db(query, data)

    def get_product(self):
        query = "SELECT * FROM products"
        return self.db.query_db(query) 

    def get_product_by_id(self, product_id):
        query = "SELECT * FROM products WHERE id = :id"
        data = {'id': product_id}
        return self.db.query_db(query, data)

    def update_product(self, product_id, product_data ):
        query = "UPDATE products SET name=:name, description=:description, price=:price WHERE id=:id"
        data = {'name':product_data['name'], 'description': product_data['description'], 'price': product_data['price'], 'id': product_id}
        return self.db.query_db(query, data)

    def delete_product(self, product_id):
        query = "DELETE FROM products WHERE id=:id"
        data = {'id': product_id}   
        return self.db.query_db(query, data)     



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