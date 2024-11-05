class Subject:

	"""Represents what is being observed"""

	def __init__(self, name =''):
		self.name = name
		self._data = 0
		self._observers = []

	def notify(self, modifier = None):

		"""Alert the observers"""

		for observer in self._observers:
			if modifier != observer:
				observer.update(self)

	def attach(self, observer):

		"""If the observer is not in the list,
		append it into the list"""

		if observer not in self._observers:
			self._observers.append(observer)

	def detach(self, observer):

		"""Remove the observer from the observer list"""

		try:
			self._observers.remove(observer)
		except ValueError:
			pass

		
	@property
	def data(self):
		return self._data

	@data.setter
	def data(self, value):
		self._data = value
		self.notify()



class Data(Subject):

	"""monitor the object"""

	def __init__(self, name =''):
		Subject.__init__(self)
		self.name = name
		self._data = 0

	@property
	def data(self):
		return self._data

	@data.setter
	def data(self, value):
		self._data = value
		self.notify()


class HexViewer:

	"""updates the Hexviewer"""

	def update(self, subject):
		print('HexViewer: Subject {} has data 0x{:x}'.format(subject.name, subject.data))

class OctalViewer:

	"""updates the Octal viewer"""

	def update(self, subject):
		print('OctalViewer: Subject' + str(subject.name) + 'has data '+str(oct(subject.data)))


class DecimalViewer:

	"""updates the Decimal viewer"""

	def update(self, subject):
		print('DecimalViewer: Subject % s has data % d' % (subject.name, subject.data))

"""main function"""

if __name__ == "__main__":

	"""provide the data"""

	obj1 = Subject('Data 1')
	obj2 = Subject('Data 2')
	print("over")

	view1 = DecimalViewer()
	view2 = HexViewer()
	view3 = OctalViewer()

	obj1.attach(view1)
	obj1.attach(view2)
	obj1.attach(view3)

	obj2.attach(view1)
	obj2.attach(view2)
	obj2.attach(view3)

	obj1.data = 10
	obj2.data = 15
