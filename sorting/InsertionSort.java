/**
 * Author - Aparna Natarajan
 * Insertion Sort - Simple way of sorting an array using insertion sort.
 * /work/code/algorithms/flaming-octo-sansa/sorting
 */
public class InsertionSort 
{
  public static void main(String[] args) 
  {
    int[] a = {7,8,9,0,5,4,3,2,1};
    
    for(int i=1; i<a.length; i++)
    {
      int temp = a[i];
      int j = i-1;
      while(j >= 0 && a[j] > temp)
      {
        a[j+1] = a[j];
        j-=1;
      }
      a[j+1] = temp;
    }
    
    for(int i=0; i<a.length; i++)
    {
      System.out.println(a[i]);
    }
  }
}