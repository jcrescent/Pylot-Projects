
from system.core.router import routes

routes['default_controller'] = 'Notes'
routes['POST']['/notes/edit/<note_id>'] = 'Notes#edit'
routes['POST']['/notes/delete/<note_id>'] = 'Notes#delete'
routes['POST']['/notes/add_note'] = 'Notes#add'