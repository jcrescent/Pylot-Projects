from system.core.controller import *

class Courses(Controller):
	def __init__(self, action):
		super(Courses, self).__init__(action)
		self.load_model('Course')

	def index(self):
		course_data = self.models['Course'].get_all_courses()
		return self.load_view('index.html',course_data=course_data)

	def add(self):
		course_data = {
			'title':request.form['name'],
			'description': request.form['description']
			}
		self.models['Course'].add_course(course_data)
		return redirect('/')

	def remove(self, course_id):
		course_data = self.models['Course'].get_courses_by_id(course_id)
		name = course_data[0]['title']
		description = course_data[0]['description']
		return self.load_view('delete.html', name=name, description=description, course_id=course_id)

	def delete(self, course_id):
		self.models['Course'].delete_course(course_id)
		return redirect('/')	

	def goback(self):
		return redirect('/')