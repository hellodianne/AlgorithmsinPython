class UnorderedList:
	#each list object will maintain a single reference to the head of the list
	#list class itself does not contain any node objects. it contains a single reference to only the first node
	#in the linked structure
	def __init__(self):
		self.head = None

	def isEmpty(self):
		#will only be true if there are no nodes in the linked list
		return self.head == None

	#since this list is unordered, the specific location of the new item with respect to the other 
	#items already in the list is not important
	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		temp.head = temp 

	#linked list traversal - Traversal refers to the process of systematically visiting each node. 
	#size = traverse the linked list and keep a count of the number of nodes that occured
	def size(self):
		current = self.head
		count = 0
		while current != None:
			count += 1
			current = current.getNext()
		return count 
	#search = traverse the linked list and check if the data stored matches the item we are looking for
	def search(self, item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True 
			else:
				current = current.getNext()
		return found 

	#remove - traverse list looking for the item we want to remove, then remove it 
	#(modify the link in the prevoise node so it refers to current)
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
		#if the item to be removed happens to be the first item in the list, then current will reference the first node 
		#in the linked list. previous will be none
		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())



