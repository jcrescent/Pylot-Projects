from system.core.controller import *

class survey_form(Controller):
	def __init__(self, action):
		super(survey_form, self).__init__(action)
	
	def index(self):
		return self.load_view('index.html')

	def result(self):
		if not 'times' in session.keys():
			session['times'] = 1
		else:
			session['times'] += 1	
		name = request.form['name']	
		location = request.form['location']
		language = request.form['language']
		comment= request.form['comment']
		return self.load_view('results.html', name=name, location=location, language=language, comment=comment)

	def back(self):
		return self.load_view('index.html')
		
		