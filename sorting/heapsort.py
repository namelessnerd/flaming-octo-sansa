#heapify


def max_heapify(list):
	n= len(list)-1
	idx= n/2

	def swap(idx1, idx2):
		tmp= list[idx1]
		list[idx1]= list[idx2]
		list[idx2]= tmp

	while idx>=0:
		print list
		# check if both children are present
		left_child= 2*idx+1
		right_child= 2*idx+2
		if left_child<n:
			if list[left_child]> list[idx] and list[left_child] > list[right_child]:
				swap(idx,left_child)
			elif list[right_child]> list[idx]:
				swap(idx,right_child)
		elif list[left_child]> list[idx]: 	
			swap(idx,left_child)
		idx-=1

def test():
	list= [6,10,1,4,7,9,3,2,8,11]
	max_heapify(list)
	print list		