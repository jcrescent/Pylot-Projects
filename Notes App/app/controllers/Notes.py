from system.core.controller import *

class Notes(Controller):
    def __init__(self, action):
        super(Notes, self).__init__(action)
        self.load_model('NotesModel')
        self.db = self._app.db
   
    def index(self):
        notes = self.models['NotesModel'].all()
        return self.load_view('notes/index.html', notes=notes)

    def edit(self, note_id):
        note_data = {'note': request.form['note'], 'id': note_id}  
        self.models['NotesModel'].update(note_data)
        notes = self.models['NotesModel'].all()
        return self.load_view('partials/notes.html', notes=notes)

    def delete(self, note_id):
        note_data = {'id': note_id}
        self.models['NotesModel'].delete(note_data)
        notes = self.models['NotesModel'].all()
        return self.load_view('partials/notes.html', notes=notes)

    def add(self):
        note_data = {'title': request.form['title']}
        self.models['NotesModel'].add(note_data)
        notes = self.models['NotesModel'].all()
        return self.load_view('partials/notes.html', notes=notes)
