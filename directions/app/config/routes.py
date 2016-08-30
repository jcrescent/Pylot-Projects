
from system.core.router import routes
routes['default_controller'] = 'Main'
routes['POST']['/main/get_directions'] = 'Main#get_directions'
