from system.core.router import routes

routes['default_controller'] = 'posts'
routes['POST']['/posts/create'] = 'posts#create'
# routes['POST']['/index_json'] = 'posts#index_json'
routes['POST']['/index_html'] = 'posts#index_html'