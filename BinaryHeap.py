#Binary Heap
#from interactivepython.org

class BinHeap:
	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0

	def swim(self, i):
		while i // 2 > 0:
			#if the new item is less than the parent
			if self.heapList[i] < self.heapList[i//2]:
				#swap the item to its parent
				tmp = self.heapList[i//2]
				self.heapList[i//2] = self.heapList[i]
				self.heapList[i] = tmp 
			i = i//2

	def insert(self, k):
		self.heapList.append(k)
		self.currentSize = self.currentSize + 1
		self.swim(self.currentSize)

	def sink(self, i):
		while (i * 2) <= self.currentSize:
			mc = self.minChild(i)
			#if the root is greater than the less child
			if self.heapList[i] > self.heapList[mc]:
				tmp = self.heapList[i]
				self.heapList[i] = self.heapList[mc]
				self.heapList[mc] = tmp 

	def minChild(self, i):
		if i * 2 + 1 > self.currentSize:
			return i * 2
		else:
			if self.heapList[i*2] < self.heapList[i*2+1]:
				return i * 2
			else:
				return i * 2 + 1

	def delMin(self):
		retval = self.heapList[1]
		#prepare move the last child to the root
		self.heapList[1] = self.heapList[self.currentSize]
		self.currentSize = self.currentSize - 1
		#delete the root
		self.heapList.pop()
		#start sinking
		self.sink(1)
		return retval

		#build an entire heap from a list of keys
	def buildHeap(self, alist):
		i = len(alist) // 2
		self.currentSize = len(alist)
		self.heapList = [0] + alist[:]
		#we start at the index
		while (i > 0):
			#and swap them until their on the right place
			self.swim(i)
			i = i -1 

