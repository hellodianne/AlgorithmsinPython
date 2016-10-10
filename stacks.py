class Stack: 
	"""Stack implementation in python"""
	def __init__(self):
		self.items = []
		
	def isEmpty(self):
		return self.items == []
	
	def push(self, item):
		self.items.append(item)
	
	def pop(self):
		#removes and return the last item on the list
		return self.items.pop()
	
	def peek(self):
		return self.items[-1]
	
	def size(self):
		return len(self.items)