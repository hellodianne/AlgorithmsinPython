class OrderedList:
	
	def __init__(self):
		self.head = None
	#isempty and size workes the same thing and remove search and add will require some modification
	#search - we stop when the item we are looking for is less than the current item
	#add - we search the spot where we need to place the node, greater than previous and less than current 
	def isEmpty(self):
		return self.head == None


	def size(self):
		current = self.head
		count = 0
		while current != None:
			count += 1
			current = current.getNext()
		return count 

	def remove(self, item):
		current = self.head
		previous = None
		found = false 
		while not found:
			if current.getData == item:
				found = True 
			else:
				previous = current
				current = current.getNext()

	def search(self, item):
		current = self.head
		found = False 
		stop = False
		while current != None and not found and not stop:
			if current.getData() == item:
				found = True 
			else:
				if current.getData() > item:
					stop = True
				else:
					current = current.getNext()
		return found 

	def add(self, item):
		current = self.head
		previous = None
		stop = False 
		while current != None and not stop:
			if current.getData() > item:
				stop = True 
			else:
				previous = current
				current = current.getNext()
		temp = Node(item)
		if previous == None:
			temp.setNext(self.head)
			self.head = temp
		else:
			temp.setNext(current)
			previous.setNext(temp)