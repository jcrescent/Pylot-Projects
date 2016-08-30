import random
from time import strftime
from system.core.controller import *


class ninja_gold(Controller):
	def __init__(self, action):
		super(ninja_gold, self).__init__(action)

	def index(self):
		if not 'gold' in session.keys():
			session['gold'] = 0
		if not 'log' in session.keys():
			session['log'] = ''
			return self.load_view('index.html')
		else:
			message = session['log']
			return self.load_view('index.html', logs = session['log'], message = message)

	def process_gold(self):
		def getGoldFrom(name, min, max):
			loot = random.randint(min,max)
			time = strftime("%b %d, %Y %I: %M %p")
			session['gold'] += loot
			if loot > 0:
				session['log'] += "<p style='color:green;'>You got "+str(loot)+" gold from the "+str(name)+"! ["+str(time)+"]</p>"
			else:
				session['log'] += "<p style='color:red;'>You got "+str(loot)+" gold from the "+str(name)+"! ["+str(time)+"]</p>"
		if request.form['place'] == 'farm_gold':
			getGoldFrom('farm', 10, 20)
		if request.form['place'] == 'cave_gold':
			getGoldFrom('cave', 5, 10)
		if request.form['place'] == 'house_gold':	
			getGoldFrom('house', 2, 5)
		if request.form['place'] == 'casino_gold':
			getGoldFrom('casino', -50, 50)	
		return redirect('/')
