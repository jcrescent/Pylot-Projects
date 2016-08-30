# """
#     Sample Controller File

#     A Controller should be in charge of responding to a request.
#     Load models to interact with the database and load views to render them to the client.

#     Create a controller using this template
# """
from system.core.controller import *

class login_reg(Controller):
    def __init__(self, action):
        super(login_reg, self).__init__(action)
        self.load_model('login_reg')

    def index(self):
        return self.load_view('index.html')

    def register(self):
        user_data = {
        'email' : request.form['email'], 
        'first_name' : request.form['first'],
        'last_name' : request.form['last'],
        'password' :  request.form['password'],
        'confirm' : request.form['confirm']
        }
        valid_check = self.models['login_reg'].register(user_data)
        print valid_check
        if valid_check['status']:
            flash('registered')
            session['id'] = valid_check['user']['id']
            session['user_first'] = valid_check['user']['first_name']
            return self.load_view('success.html')
        else:
            for message in valid_check['invalids']:
                flash(message)
            return redirect('/')

    def get_user(self):
        user_data = {
        'email': request.form['email'],
        'password': request.form['password']
        }   
        user = self.models['login_reg'].get_user(user_data)
        print query_result
        if user:
            session['id'] = query_result[0]['id']
            session['user_first'] = query_result[0]['first_name']
            return self.load_view('admin_dashboard')
        else:
            return redirect('/')    