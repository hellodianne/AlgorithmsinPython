class QuickFindUF(object):
	"""
	Quick Find eager approach
	"""

	def __init__(self, num):
		"""
		Initialize data structure, 
		set id for 0 to num  
		"""
		self.num = num 
		self.id = [i for i in range(self.num)]
	
	def getId(self):
		return self.id

	def connected(self, p, q):
		"""
		element p and q are connected if both have the same id
		"""
		return self.id[p] == self.id[q]

	def union(self, p, q):
		"""
		to connect p and q, for all entries whose id is p, 
		change its id to q 
		"""
		idP = self.id[p]
		idQ = self.id[q]
		#all element with this id will change all their ids
		for i in range(len(self.id)):
			if self.id[i] == idP: #look for the entries whose id is equal to the id of the 1st argument
				self.id[i] = idQ 



