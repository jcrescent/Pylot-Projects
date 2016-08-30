
from system.core.controller import *

class Book_review(Controller):
    def __init__(self, action):
        super(Book_review, self).__init__(action)
        self.load_model('Book_reviewModel')
      
     
    def index(self):
        return self.load_view('index.html')

    def registration(self):
        user_data = {
            'name' : request.form['name'],
            'alias' : request.form['alias'],
            'email' : request.form['email'],
            'password' : request.form['password']
        }

        valid_check = self.models['Book_reviewModel'].register(user_data)
        if valid_check: 
            session['id'] = valid_check['user']['id']
            session['user_first'] = valid_check['user']['first_name']
            return self.load_view('home.html')
        else: 
            flash(valid check)
            return redirect('/')

    def add_book_page(self);
        return self.load_view('add_book_and_review.html')       

    def add_book_review(self):
        book_data = {
            'title' : request.form['name'], 
            'author' : request.form['alias']
            }
        review_data = {            
            'review' : request.form['email'],
            'rating' : request.form['password'],
            'user_id' : session['id']
        } 
        self.models['Book_reviewModel'].create_book_review(book_data, review_data)
        return self.load_view('show.html')

    def home(self):
        recent_reviews = self.models['book_reviewModel'].get_recent_reviews()
        all_books = self.models['book_reviewModel'].get_all_reviews()
        return self.load_view('home.html', recent_reviews=reviews, all_books=all_books)

    def show_book(self, book_id):
        reviews = self.models['book_reviewModel'].get_book_reviews(book_id)
        title = book_data[0]['title']
        return self.load_view('show.html', title=title, reviews=reviews)
            
    def view_user(self):
