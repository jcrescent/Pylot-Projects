from system.core.model import Model

class NotesModel(Model):
    def __init__(self):
        super(NotesModel, self).__init__()
   
    def all(self):
        query = "SELECT * FROM notes"
        return self.db.query_db(query)

    def update(self, note_data):
        query = "UPDATE notes SET note = ':note', updated_at =':NOW()' WHERE id = :id"
        data = { 'note' : note_data['note'], 'id' : note_data['id']}
        self.db.query_db(query,data)

    def delete(self, note_data):
        query = "DELETE FROM notes WHERE id = :id"
        data = { 'id' : note_data['id']}
        self.db.query_db(query, data)

    def add(self, note_data):
        query = "INSERT INTO notes(title, note, created_at, updated_at) VALUES (:title, :note, NOW(), NOW())"
        data = {'title': note_data['title'], 'note': 'Edit note text'} 
        self.db.query_db(query, data)  