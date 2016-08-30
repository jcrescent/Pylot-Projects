from system.core.controller import *
class Main(Controller):
    def __init__(self, action):
        super(Main, self).__init__(action)
    def index(self):
        return self.load_view('main/index.html')

    def get_directions(self):
        origin = request.form['origin']
        destination = request.form['destination']
        # gps = "https://maps.googleapis.com/maps/api/js?key=AIzaSyCOSc4mFEPVmEzfMlBildeFNCD-RU51-0s&callback=initMap"
        url ='https://maps.googleapis.com/maps/api/directions/json?origin='+origin+'&destination='+destination+'&key=AIzaSyCOSc4mFEPVmEzfMlBildeFNCD-RU51-0s'
        response = requests.get(url).content
        print response
        return response

# https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=(pos)&radius=500&keyword=(what do you want to do result)&name=cruise&key=YOUR_API_KEY
    def place_search(self):
        location = request.form['location']
        what = request.form['what']
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+location+"&radius=500&keyword="+what+"&key=AIzaSyBLgLT2H_qbHsAKH6L6Da_aLyz-aRGG34U"
        response = requests.get(url).content
        return response