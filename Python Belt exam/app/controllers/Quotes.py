
from system.core.controller import *

class Quotes(Controller):
    def __init__(self, action):
        super(Quotes, self).__init__(action)
        self.load_model('QuotesModel')
        self.db = self._app.db
   
    def index(self):
        return self.load_view('index.html')

    def register(self):
        user_data = {
            'name' : request.form['name'],
            'alias' : request.form['alias'], 
            'email' : request.form['email'],
            'password' :  request.form['password'],
            'confirm' : request.form['confirm'],
            'dob': request.form['dob']
            }
        valid_check = self.models['QuotesModel'].registration(user_data)
        if valid_check['status']:
            session['id'] = valid_check['user']['id']
            session['alias'] = valid_check['user']['alias']
            return redirect('/quotes')
        else:
            for message in valid_check['invalids']:
                flash(message)
            return redirect('/')   

    def login(self):
        user_data = {
        'email': request.form['email'],
        'password': request.form['password']
        }   
        user = self.models['QuotesModel'].get_user(user_data)
        if user:
            session['id'] = user['id']
            session['alias'] = user['alias']
            return redirect('/quotes')
        else:
            flash("Incorrect password or email")
            return redirect('')   

    def logout(self):
        session.clear()
        return redirect('/')         

    def add_quote(self):
        quote_data= {
            'author' : request.form['author'],
            'quote' : request.form['quote'],
            'creator_id' : session['id']
            }
        valid_check = self.models['QuotesModel'].create_quote(quote_data)
        if valid_check['status']:
            return redirect('/quotes')
        else:
            for message in valid_check['invalids']:
                flash(message)
            return redirect('/quotes')        

    def add_favorites(self, quote_id):
        favorites_data = {
            'quote_id' : quote_id,
            'user_id': session['id']
        }
        self.models['QuotesModel'].add_to_favorites(favorites_data) 
        
    def display_quotes(self):
        quotes = self.models['QuotesModel'].get_recent_quotes()
        # favorites = self.models['QuotesModel'].get_favorites(session['id'])
        print quotes
        # print favorites
        return self.load_view('quotes.html', quotes = quotes)

    def view_user(self, user_id):
        user_quotes = self.models['QuotesModel'].get_user_by_id(user_id)
        return self.load_view('user.html', user_quotes=user_quotes)    

    def dashboard(self):
        return redirect('/dashboard')