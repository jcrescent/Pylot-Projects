
from system.core.controller import *
class Main(Controller):
    def __init__(self, action):
        super(Main, self).__init__(action)
    def index(self):
        return self.load_view('main/index.html')

    def get_directions(self):
    	origin = request.form['origin']
    	destination = request.form['destination']
    	url ='https://maps.googleapis.com/maps/api/directions/json?origin='+origin+'&destination='+destination+'&key=AIzaSyCOSc4mFEPVmEzfMlBildeFNCD-RU51-0s'
    	response = requests.get(url)
    	print response

        # artist = request.form['user_input'].replace(' ', '')
        # url = "https://itunes.apple.com/search?term=" + artist + "&entity=musicVideo"
        # response = requests.get(url).content
        # return response

