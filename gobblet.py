
class Gobblet(object):

	def __init__(self, color,size):
		self.color = color
		self.size = size


	def setSize(self,size):
		if (size > 4):
			self.size = 4
		
		elif(size < 0):
			self.size = 0

		else:
			self.size = size

	def color(self,color):
		return self.color


	def size(self):
		return self.size
