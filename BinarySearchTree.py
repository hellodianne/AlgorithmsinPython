#implementation of BinarySearchTree
#reference: interactivepython.org 6.13

class TreeNode:
	def __init__(self, key, val, left = None, right = None, parent = None):
		self.key = key
		self.value = val
		self.leftChild = left
		self.rightChild = right 
		self.parent = parent 


class BinarySearchTree:
	def __init__(self):
		self.root = None
		self.size = 0

	def length(self):
		return self.size

	def insert(self, key, val):
		if self.root:
			self._insert(key, val, self.root)
		else:
			self.root = TreeNode(key, val)
		self.size = self.size + 1

	def _insert(self, key, val, currentNode):
		if key < currentNode.key:
			if currentNode.leftChild != None:
				self._insert(self, key, val, currentNode.leftChild)
			else:
				currentNode.leftChild = TreeNode(key, val, parent=currentNode)
		else:
			if currentNode.rightChild != None:
				self._insert(self, key, val, currentNode.rightChild)
			else:
				currentNode.rightChild = TreeNode(key, val, parent=currentNode)

	def get(self, key):
		if self.root:
			res = self._get(key, self.root)
			if res:
				return res.value
			else:
				return None

	def _get(self, key, currentNode):
		if not currentNode:
			return None
		elif currentNode.key == key:
			return currentNode
		elif key < currentNode.key:
			return self._get(self, key, currentNode.leftChild)
		else:
			return self._get(self, key, currentNode.rightChild)

	def delete(self, key):
		if self.size > 1:
			nodeToRemove = self._get(key, self.root)
			if nodeToRemove:
				self.remove(nodeToRemove)
				self.size = self.size - 1
			else:
				raise KeyError('Error, key not in tree')
		elif self.size == 1 and self.root.key == key:
			#we return an empty tree
			self.root = None
			self.size = self.size - 1
		else: 
			raise KeyError('Error, key not in tree')

	def findMin(self):
		current = self
		if self.rightChild != None:
			current = self
			while current.leftChild != None:
				current = current.leftChild
		return current 
		


	def remove(self, currentNode):
		#if the node is a leaf
		if currentNode.rightChild == None and currentNode.leftChild == None:
			#if it is the left child
			if currentNode == currentNode.parent.leftChild:
				currentNode.parent.leftChild = None
			#if it is the right child
			else:
				currentNode.parent.rightChild = None
		#if the node has both child
		elif currentNode.rightChild != None and currentNode.leftChild != None:
			delNode = currentNode.findMin()
			delNodeParent = delNode.parent 
			currentNode.val = delNode.val
			currentNode.key = delNode.key 
			delNodeParent.leftChild = None 
		#if node has only one child
		else:
			#if node has left child only
			if currentNode.leftChild != None and currentNode.rightChild == None:
				#and it is THE LEFT CHILD
				if currentNode.parent.leftChild == currentNode:
					currentNode.leftChild.parent = currentNode.parent 
					currentNode.parent.leftChild = currentNode.leftChild
				#and it is THE RIGHT CHILD
				elif currentNode.parent.rightChild == currentNode:
					 currentNode.leftChild.parent = currentNode.parent 
					 currentNode.parent.rightChild = currentNode.leftChild
				#else it must be the root, to follow
			else:
				if currentNode.isLeftChild():
					currentNode.rightChild.parent = currentNode.parent
					currentNode.parent.leftChild = currentNode.rightChild
				elif currentNode.isRightChild():
					currentNode.rightChild.parent = currentNode.parent
					currentNode.parent.rightChild = currentNode.rightChild
				#else it must be the root, to follow

