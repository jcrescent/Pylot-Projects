
from system.core.router import routes

routes['default_controller'] = 'Quotes'
routes['POST']['/register'] = 'Quotes#register'
routes['POST']['/login'] = 'Quotes#login'
routes['POST']['/logout'] = 'Quotes#logout'
routes['GET']['/quotes'] = 'Quotes#display_quotes'
routes['POST']['/add_quote'] ='Quotes#add_quote'
routes['POST']['/add_fav/<quote_id>'] = 'Quotes#add_favorites'
routes['GET']['/users/<user_id>'] = 'Quotes#view_user'
routes['GET']['/dashboard'] = 'Quotes#display_quotes'