/**
 * Author - Aparna Natarajan
 * Collection Sort - Simple way of sorting an array using Collection sort.
 * For simplicity sake we are assuming that the range of values in the integer array is between 0 and 9.
 * Generally we take it by assuming that it is a char array and with length 256. 
 * /work/code/algorithms/flaming-octo-sansa/sorting
 */
public class CountingSort 
{
  public static void main(String[] args) 
  {
    int[] a = {7,8,9,0,5,4,3,2,1};
    int[] op = new int[a.length];
    int[] count = new int[10];

    for(int i=0; i<count.length; i++)
    {
      count[i] = 0;
    }

    for(int i=0; i<a.length; i++)
    {
      count[a[i]]++;
    }

    for(int i=1; i<count.length; i++)
    {
      count[i] += count[i-1];
    }

    for(int i=0; i<a.length; i++)
    {
      op[count[a[i]] - 1] = a[i];
    }

    for(int i=0; i<op.length; i++)
    {
      System.out.println(op[i]);
    }
  }
}