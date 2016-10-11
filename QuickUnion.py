class QuickUnionUF(object):
    
    def __init__(self, num):
        self.num = num
        self.id = [i for i in range(self.num)]
       
    
    def getId(self):
        return self.id
    
    def getRoot(self, p):
	"""
	chase parent pointers until reach root
	"""
	root = self.id[p] #value of id at pth position
	while root != self.id[root]: #while root is not equal to the value of id at the root position
	    root = self.id[root]
	return root
    
    def connected(self, p , q):
        return self.getRoot(p) == self.getRoot(q)
    
    def union(self, p, q):
        """
        change root of p to point to root of q
        change parent of p to parent of q 
        #change the value of ith position to j
        """
        j = self.getRoot(q)
        i = self.getRoot(p)
        #set root of p to root of q
        #somethings wrong here //changed to nothings wrong here
        self.id[i] = j






