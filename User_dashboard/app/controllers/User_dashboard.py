"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class User_dashboard(Controller):
    def __init__(self, action):
        super(User_dashboard, self).__init__(action)

        self.load_model('DashboardModel')
   
    def index(self):
        return self.load_view('index.html')

    def login(self):
        user_data = {
            'email': request.form['email'],
            'password' : request.form['password']
        }
        user = self.models['dashboardModels'].get_user(user_data)
        if user:
            session['id'] = user[0]['id']
            session['user_first'] = user[0]['first_name']
            return redirect('/admin_dashboard')
        else:
            flash("Email or password incorrect")    

    def registration(self):
        return self.load_view('register.html')

    def register(self):
        user_data = {
            'first_name' : request.form['first'],
            'last_name' : request.form['last'],
            'email' : request.form['email'],
            'password' : request.form['password'],
            'confirm' : request.form['confrim']
        }
        valid_check = self.models['dashboardModel'].register(user_data)
        if valid_check['status']:
            all_users = valid_check['all_users']
            session['id'] = valid_check['user']['id']
            session['user_first'] = valid_check['user']['first_name']
            return redirect('/admin_dashboard')
        else:
            for message in valid_check['invalids']:
                flash(message)
            return redirect('/register') 

    def admin_dashboard(self):
        all_users = self.models['dashboardModels'].get_users()
        return self.load_view('admin_dashboard.html', all_users=all_users)

    def show_wall(self, user_id):
        user_info = self.models['dashboardModel'].get_user_by_id(user_id)
        messages_info = self.models['dashboardModel'].get_messages_by_id(user_id)
        comments_info = self.models['dashboardModel'].get_comments_by_id(messages)
        return self.load_view('user_wall.html', user_info=user_info, messages_info=message)

    def post_message(self, user_id):
        message_info = {
            'user_id' : session['id'],
            'message' : request.form['message'],
            'wall' : user_id
        }
        self.models['dashboardModel'].add_message(message_info)
        return redirect('/wall/<user_id>')

    def post_comment(self, message_id, user_id):
        comments_info = {
            'user_id' : session['id'],
            'comment' : request.form['comment'],
            'message_id' : message_id 
        } 
        self.models['dashboardModel'].add_comment(comment_info)
        return redirct('/wall/<user_id>')    