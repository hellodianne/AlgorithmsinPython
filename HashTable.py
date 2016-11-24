#reference: interactivepython.org 5.5
class HashTable:
	def __init__(self):
		#initial size for is arbitrary but should be a prime number
		self.size = 11
		self.slots = [None] * self.size 
		self.data = [None] * self.size 

	def hashfunction(self, key, size):
		return key%size

	def rehash(self, oldhash, size):
		#linear probing
		return (oldhash+1)%size 

	def put(self, key, data):
		hashvalue = self.hashfunction(key, len(self.slots))

		if self.slots[hashvalue] == None:
			self.slots[hashvalue] = key
			self.data[hashvalue] = data
		else:
			if self.slots[hashvalue] == key:
				self.data[hashvalue] = data #replace
			else:
				nextslot = self.rehash(hashvalue, len(self.slots))
				while self.slots[nextslot] != None and self.slots[nextslot] != key:
					nextslot = self.rehash(nextslot, len(self.slots))

				if self.slots[nextslot] == None:
					self.slots[nextslot] = key 
					self.data[nextslot] = data
				else:
					self.data[nextslot] = data #replace

	def get(self, key):
		startslot = self.hashfunction(key, len(self.slots))

		data = None
		stop = False 
		found = False
		position = startslot

		while self.slots[position] != None and not found and not stop:
			if self.slots[position] == key:
				found = True
				data = self.data[position]
			else:
				position = self.rehash(position, len(self.slots))
				if position == startslot:
					stop = True
		return data 






