/**
 * Author - Aparna Natarajan
 * Quick Sort - Simple way of sorting an array using quick sort.
 * /work/code/algorithms/flaming-octo-sansa/sorting
 */

 public class QuickSort
 {
 	static int[] a = {9,5,4,3,8,7,2,5,1,0,-2,-1};
 	public static void main(String args[])
 	{
 		quickSortA(0, a.length-1);

 		for(int i=0; i<a.length; i++)
 		{
 			System.out.println(a[i]);
 		}
 	}

 	public static void quickSortA(int low, int high)
 	{
 		int mid = low + (high-low)/2;
 		int pivot = a[mid];
 		int i=low; 
 		int j=high;

 		while(i <= j)
 		{
 			while(a[i] < pivot) i++;
 			while(a[j] > pivot) j--;

 			if(i<=j)
 			{
 				int temp = a[i]; 
 				a[i] = a[j];
 				a[j] = temp;
 				i++;
 				j--;
 			}
 		}

 		if(low <= j)
 			quickSortA(low, j);
 		if(i <= high)
 			quickSortA(i, high);
 	}
 }