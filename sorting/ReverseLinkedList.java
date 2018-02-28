public class ReverseLinkedList
{
    public static void main(String args[])
    {
        Node head = new Node(5, new Node(3, new Node(2, new Node(1,null))));
        Node sorted = sortLLIter(head);
        System.out.println("\nIterative reverse LL: ");
        
        while(sorted != null)
        {
            System.out.println(sorted.data);
            sorted = sorted.next;
        }
        
        System.out.println("\nRecursive reverse LL: ");
        head = new Node(5, new Node(3, new Node(2, new Node(1,null))));
        Node reversed = sortLLRecur(head);
        while(reversed != null)
        {
            System.out.println(reversed.data);
            reversed = reversed.next;
        }
    }
    
    public static Node sortLLIter(Node head)
    {
        Node curr = head; 
        Node prev = null;
        Node next = head;
        
        while(curr != null)
        {
            next = curr.next;
            curr.next = prev;
            prev = curr; 
            curr = next;
        }
        
        return prev;
    }
    
    public static Node sortLLRecur(Node head)
    {
        if(head == null || head.next == null)
            return head;
        Node second = head.next;
        head.next = null;
        
        Node rev = sortLLRecur(second);
        second.next = head;
        
        return rev;
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