class WeightedQuickUnionUF:

	def __init__(self, num):
		self.num = num
		self.id = [i for i in range(self.num)]
		self.sz = [1 for i in range(self.num)]

	def getId(self):
		return self.id

	def getSz(self):
		return self.sz 

	def getRoot(self, p):
		"""same as quickunion"""
		root = self.id[p]
		while root != self.id[root]:
			root = self.id[root]
		return root 

	def connected(self, p, q):
		return self.getRoot(p) == self.getRoot(q)

	def union(self, p, q):
		"""
		link root of smaller tree to root of larger tree
		update the sz[] array
		"""
		i = self.getRoot(p)
		j = self.getRoot(q)
		
		if i == j:
			return

		if self.sz[i] < self.sz[j]:
			self.id[i] = j
			self.sz[j] += self.sz[i]
		else:
			self.id[j] = i
			self.sz[i] += self.sz[j]




