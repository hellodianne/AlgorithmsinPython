class Queue:
	def __init__(self):
		self.items = []
	
	def isEmpty(self):
		return self.items == []
	
	def enqueue(self, item):
		#add item at the end of the queue 
		self.items.append(item)
	
	def dequeue(self):
		#return and remove the item at the beginning of the queue 
		return self.items.pop(0)
	def size(self):
		return len(self.items)