
'''
This is merge sort implementation. Merge sort takes a list and splits the list into two, left and right.
 These are again recursively split, until we have lists with 1 element each.
These lists are merged by the merge_left_right method. The main intuition behind the merge is that given 
two sorted lists, one can create a merged sorted list in o(n).
The merge_left_right method checks if the head of left list is less than or equal to (ascending order sort) 
the head of the right list. Since these two are sorted lists, 
if the head of the left list is LEQ head of right list, all of the right list is GEQ to this element. 

The time complexity is nlog(n). Merge sort has a space complexity of o(n) + o(log n) (to keep stack frames 
in recurson), yielding o(n) as it does not do in place sort.

The mergetuple_left_right method takes a list of tuples and a position argument by which this must be sorted. 
For example, to sort a list of strings by their length, 
one can first create a tuple that of the format (string length, position in list). 
The merge_sort method then sorts the strings by length. Since we are saving the position 
in the original list, one could create a set of strings sorted by their length.

The code for this would be:

	sorted_string=[list_of_strings[sorted_tuple[1]] for sorted_tuple in merge_sort([(len(v),k) for k,v in enumerate(list_of_strings)], type='tuple')].

test methods: test_string_list and test_short_list
'''
import random

def merge_sort(list, type=None, pos=0):
	len_list= len(list)
	if len_list<=1:
		return list
	left= merge_sort(list[:len_list/2])
	right= merge_sort(list[len_list/2:])
	if type=='tuple':
		try:
			return mergetuple_left_right(left, right, pos)
		except IndexError, e:
			raise e
	else:
		return merge_left_right(left, right)

def merge_left_right(left, right):
	len_left= len(left)
	len_right= len(right)
	result=[]
	while len_left >0 or len(right):
		if len_left and len_right:
			if left[0] <= right[0]:
				result.append(left[0])
				left=left[1:]
			else:
				result.append(right[0])
				right= right[1:]
		elif len_left:
			result.extend(left)
			left=[]
		elif len_right:
			result.extend(right)
			right=[]
		len_left= len(left)
		len_right= len(right)
	return result

def mergetuple_left_right(left, right, pos):
	len_left= len(left)
	len_right= len(right)
	result=[]
	while len_left >0 or len(right):
		if len_left and len_right:
			try:
				if left[0][pos] <= right[0][pos]:
					result.append(left[0])
					left=left[1:]
				else:
					result.append(right[0])
					right= right[1:]
			except IndexError, e:
					raise
		elif len_left:
			result.extend(left)
			left=[]
		elif len_right:
			result.extend(right)
			right=[]
		len_left= len(left)
		len_right= len(right)
	return result

def test_string_list():
	print 'This method tests merge sort with a list of strings that need to be sorted by their string length'
	list_of_strings= ['cat', 'cab', 'bat', 'bark', 'bard', 'cow', 'as']
	print 'List before sorting: {0}'.format(list_of_strings)
	sorted_string=[list_of_strings[sorted_tuple[1]] for sorted_tuple in merge_sort
		([(len(v),k) for k,v in enumerate(list_of_strings)], type='tuple')]

def test_short_list():
	print 'This method tests merge sort with a list of 100 integers'
	list_of_int= [random.randint(0,100) for i in range(100)]
	print 'List before sorting: {0}'.format(list_of_int)
	print 'List after sorting: {0}'.format(merge_sort(list_of_int))

def main():
	test_short_list()

if __name__ == '__main__':
	main()
