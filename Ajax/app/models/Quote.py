from system.core.model import Model

class Quote(Model):
    def __init__(self):
        super(Quote, self).__init__()
        
    def all(self):
        query = "SELECT * FROM quotes"
        return self.db.query_db(query)

    def create(self, new_quote):
       query = "INSERT INTO quotes (author, quote) VALUES (:author, :quote)"
       data = { 'author': new_quote['author'], 'quote': new_quote['quote'] }
       return self.db.query_db(query, data)    