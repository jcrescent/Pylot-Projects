# """
#     Sample Controller File

#     A Controller should be in charge of responding to a request.
#     Load models to interact with the database and load views to render them to the client.

#     Create a controller using this template
# """
from system.core.controller import *

class products(Controller):
    def __init__(self, action):
        super(products, self).__init__(action)
        self.load_model('productsModel')
   
    def index(self):
        all_products = self.models['productsModel'].get_product()
        if all_products:
            return self.load_view('index.html', all_products=all_products)
        else:
            return self. load_view('index.html')

    def new(self):
        return self.load_view('create.html')

    def add_product(self):
        product_data = {
            'name' : request.form['name'],
            'description' : request.form['description'], 
            'price' : request.form['price'] 
        }
        self.models['productsModel'].add_product(product_data)
        return redirect('/')

    def show(self, product_id):
        product_info = self.models['productsModel'].get_product_by_id(product_id)
        return self.load_view('show.html', product_info = product_info[0]) 

    def edit(self, product_id):
        return  self.load_view('edit.html', product_id = product_id)

    def update(self, product_id):
        product_data = {
            'name' : request.form['name'],
            'description' : request.form['description'], 
            'price' : request.form['price'] 
        }
        self.models['productsModel'].update_product(product_id, product_data)
        return redirect('/') 

    def remove(self, product_id):
        self.models['productsModel'].delete_product(product_id)
        return redirect ('/')






    

        # """
        # A loaded model is accessible through the models attribute 
        # self.models['WelcomeModel'].get_users()
        
        # self.models['WelcomeModel'].add_message()
        # # messages = self.models['WelcomeModel'].grab_messages()
        # # user = self.models['WelcomeModel'].get_user()
        # # to pass information on to a view it's the same as it was with Flask
        
        # # return self.load_view('index.html', messages=messages, user=user)
        # """
       

