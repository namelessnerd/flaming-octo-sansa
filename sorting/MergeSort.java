
/*
 * Author - Aparna Natarajan
 * Merge Sort - Simple way of sorting an array using merge sort.
 * /work/code/algorithms/flaming-octo-sansa/sorting
 */

public class MergeSort 
{
  static int[] a = {7,8,9,0,5,4,3,2,1, -2, -1};
  public static void main(String[] args) 
  {
    mergeSortA(0, a.length-1, new int[a.length]);
    
    for(int i=0; i<a.length; i++)
    {
      System.out.println(a[i]);
    }
  }
  
  public static void mergeSortA(int low, int high, int[] temp)
  {
    if(low < high)
    {
      int mid = low + (high-low)/2;
      mergeSortA(low, mid, temp);
      mergeSortA(mid+1, high, temp);
      merge(low, mid, high, temp);
    }
  }
  
  public static void merge(int low, int mid, int high, int[] temp)
  {
    for(int i=low; i<=high; i++)
    {
      temp[i] = a[i];
    }
    
    int i = low; 
    int j = mid + 1;
    int k = low;
    
    while(i <= mid && j <= high)
    {
      if(temp[i] <= temp[j])
      {
        a[k] = temp[i];
        i++;
        k++;
      }
      else if (temp[i] > temp[j])
      {
        a[k] = temp[j];
        j++;
        k++;
      }
    }
    
    while(i <= mid)
    {
      a[k] = temp[i];
      i++;
      k++;
    }
  }
}