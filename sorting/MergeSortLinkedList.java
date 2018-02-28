public class MergeSortLinkedList 
{
  public static void main(String args[])
  {
    Node head = new Node(0, new Node(5, new Node(4, new Node(3, null))));
    
    Node temp = mergeSortLL(head);
    while(temp != null)
    {
      System.out.println(temp.data);
      temp = temp.next;
    }
  }
  
  public static Node mergeSortLL(Node head)
  {
    if(head == null || head.next == null)
      return head;
    
    // Dividing it using the fast-slow pointer technique
    Node l = head;
    Node r = head;
    while(r.next!= null && r.next.next!= null)
    {
      l = l.next;
      r = r.next.next;
    }
    
    r = l;
    l = head;
    
    // call merge sort on the left and right sections of the linkedlist
    mergeSortLL(l);
    mergeSortLL(r);
    Node temp = mergeLL(l,r);
    
    return temp;
  }
  
  public static Node mergeLL(Node left, Node right)
  {
    Node temp = null;
    
    while(left.next != null && left.next != null)
    {
      if(left.data < right.data)
      {
        temp = left;
        temp.next = mergeLL(left.next, right);
      }
      else
      {
        temp = right;
        temp.next = mergeLL(left, right.next);
      }
    }
    return temp;
  }
}

class Node
{
  int data;
  Node next;
  
  public Node(int data)
  {
    this.data = data;
    this.next = null;
  }
  
  public Node(int data, Node next)
  {
    this.data = data;
    this.next = next;
  }
}