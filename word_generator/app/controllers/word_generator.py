import string, random
from system.core.controller import *

class word_generator(Controller):
	def __init__(self, action):
		super(word_generator, self).__init__(action)

	def index(self):
		session['count'] = 0
		return self.load_view('index.html')

	def process(self):
		session['count'] += 1
		word = ''
		for x in range (14):
			word += random.choice(string.ascii_letters)
		return self.load_view('index.html', word=word)