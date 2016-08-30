from system.core.model import Model

class postsModel(Model):
    def __init__(self):
        super(postsModel, self).__init__()

    def all(self):
       query = "SELECT * FROM posts"  
       return self.db.query_db(query)  
   
    def create(self, post_data):
        query = "INSERT INTO posts(description, created_at, updated_at) VALUES (:description, NOW(), NOW())"
        data = { 'description' : post_data['note']}
        return self.db.query_db(query, data)
