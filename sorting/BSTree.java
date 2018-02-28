import java.util.Queue;
import java.util.Stack;

public class BSTree
{
    public static void main(String args[])
    {
        Node head = new Node(5, new Node(3, new Node(2), new Node(4)), new Node(7, new Node(6), new Node(9)));
        breadthFirstTraversal(head);
    }
    
    public static void breadthFirstTraversal(Node head)
    {
        Queue<Node> que = new Queue<Node>();
        que.offer(head);
        while(!que.isEmpty())
        {
            Node temp = que.poll();
            System.out.println(temp.data);
            
            que.offer(temp.left);
            que.offer(temp.right);
        }
    }
    
    public static void depthFirstTraversal(Node head)
    {
        Stack<Node> stk = new Stack<Node>();
        stk.push(head);
        while(!stk.isEmpty())
        {
            Node temp = stk.pop();
            stk.push(temp.right);
            stk.push(temp.left);
            
            System.out.println(temp.data);
        }
    }
    
    // using recursion
    public static void inOrderTraversal(Node head)
    {
        //left-data-right
        if(head == null) return;
        
        inOrderTraversal(head.left);
        System.out.println(head.data);
        inOrderTraversal(head.right);
    }

    // using recursion
    public static void preOrderTraversal(Node head)
    {
        //data-left-right
        if(head == null) return;
        
        System.out.println(head.data);
        preOrderTraversal(head.left);
        preOrderTraversal(head.right);
    }

    // using recursion
    public static void postOrderTraversal(Node head)
    {
        //left-right-data
        if(head == null) return;
        
        postOrderTraversal(head.left);
        postOrderTraversal(head.right);
        System.out.println(head.data);
    }

    public static int findDepthOfBinTree(Node head)
    {
        if(head == null)
            return 0;
        return 1 + Max(findDepthOfBinTree(head.left), findDepthOfBinTree(head.right));
    }

    public static int findSizeOfBinTree(Node head)
    {
        if(head == null) return 0;
        return 1 + findSizeOfBinTree(head.left) + findSizeOfBinTree(head.right);
    }

    public static boolean checkIdenticalTree(Node tree1, Node tree2)
    {
        if(tree1 == null && tree2 == null) return true;
        return tree1.data == tree2.data && checkIdenticalTree(tree1.left, tree2.left) && checkIdenticalTree(tree1.right, tree2.right);
    }

    public static void deleteNode(Node head)
    {
        if(head == null) return;
        deleteNode(head.left);
        deleteNode(head.right);
        head = null;
    }

    public static Node convertToMirror(Node head)
    {
        if(head == null) return head;
        Node left = convertToMirror(head.left);
        Node right = convertToMirror(head.right);
        
        head.left = right;
        head.right = left;
        
        return head;
    }

    public static int getLeafCount(Node head)
    {

    }

    public static Node lowestComAncestorBST(Node root, int n1, int n2)
    {
        if(root == null) return null;
        
        while(root != null)
        {
            if(root.data > n1 && root.data > n2)
            {
                root = root.left;
            }
            else if(root.data < n1 && root.data < n2)
            {
                root = root.right;
            }
            else
            {
                return root;
            }
        }
    }
    
}

class Node
{
    int data;
    Node left; 
    Node right;
    
    public Node(int data)
    {
        this.data = data;
        this.left = null;
        this.right = null;
    }
    
    public Node(int data, Node left, Node right)
    {
        this.data = data;
        this.left = left;
        this.right = right;
    }
}