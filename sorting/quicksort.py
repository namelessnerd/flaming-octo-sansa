'''
Quicksort is a divide and conquer algorithm. In Quicksort, a pivot element is 
chosen and the list is divided into two halves: to the left of the pivot with all values
smaller than the pivot and to the right of the pivot, with all other values, including 
that of the pivot (if it appears multiple times). The left is sorted and the right list 
is sorted. 

Pivot and Partition(create partition method): 
This is the critical method in quicksort. To create the partition, we identify the pivot. 
Starting from both the ends, traverse the list. From the left, skip elements that are 
less than the pivot and from the right, skip elements that are greater than the pivot. 
If we have an element in left that is greater than the pivot AND an element that is either 
equal or less than the pivot to the right, swap them. 
Terminate once the left side marker crosses the right side marker and return the left side 
market.

Call quicksort on the sublist terminating at the left side marker and on rest of the list 
(Starting one position to the right of the marker)

Like all divide and conquer algorithms, the time complexity of Quicksort is calculated by 
a recurrence relation. The relation for Quicksort is: T(n)= 2T(n/2) + O(n), ie. the time 
complexity of the sort is the sum of the time complexity for sorting each of the halves, plus
the time complexity to find the pivot. 

Pivot selection affects the performance of the algorithm. In worst case, Quicksort can be O(n2),
when repeatedly extreme pivots are chosen (the largest or smallest element). The best approach 
to select a pivot is to select the median element (one that has half of the list less than itself).
The common practise is to just pick the middle element of the list. 

Even though other algorithms have better worst case, with same average case, Quicksort has been 
proven to be efficent in practice. 
The Quicksort algorithm below derives from CLR approach. 
'''

def create_partition(list, low, high):
	pivot= list[(low+ high)/2]
	while low< high:
		while list[low]<pivot:
			low+=1
		while list[high]>pivot:
			high-=1
		if low <= high:
			tmp= list[low]
			list[low]= list[high]
			list[high]= tmp
			low+=1
			high-=1
	return low


def quicksort(list, low, high):
	if low< high:
		idx= create_partition(list, low, high)
		print list
		quicksort(list, low, idx-1)
		quicksort(list,idx, high)

def test():
	list= [1, 12, 5, 26, 7, 14, 3, 7, 2,]
	quicksort(list, 0, 8)
	print list

def main():
	test()

if __name__ == '__main__':
	main()