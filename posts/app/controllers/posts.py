from system.core.controller import *

class posts(Controller):
    def __init__(self, action):
        super(posts, self).__init__(action)

        self.load_model('postsModel')
        self.db = self._app.db

   
    def index(self):
        posts = self.models['postsModel'].all()
        return self.load_view('posts/index.html', posts=posts)

    def index_json(self):
        posts = self.models('postsModel').all()
        return jsonify(posts=posts)

    def index_html(self):
        posts = self.models('postsModel').all()
        return self.load_view('partials/posts.html', posts = posts)   

    def create(self):
        post_data = {'note' : request.form['note']} 
        self.models['postsModel'].create(post_data) 
        posts = self.models['postsModel'].all()  
        return self.load_view('partials/posts.html', posts=posts)
