def quickSort(a):
	sortingFunc(a, 0, len(a)-1)

def sortingFunc(a, lo, hi):
	if hi <= lo:
		return 
	j = partition(a, lo, hi)
	sortingFunc(a, lo, j-1)
	sortingFunc(a, j+1, hi)

def partition(a, lo, hi):
	i = lo + 1
	j = hi 
	while True:
		#find item on left to swap
		while a[i] < a[lo]:
			if i == hi:
				break
			i+=1
		#find item on right to swap
		while a[lo] < a[j]:
			if j == lo:
				break
			j-=1
		#check if pointers cross
		if(i>=j):
			break
		#swap
		exch(a, i, j)
	
	#swap with partitioning item
	exch(a, lo, j)
	return j

def exch(a, i, j):
	swap = a[i]
	a[i] = a[j]
	a[j] = swap