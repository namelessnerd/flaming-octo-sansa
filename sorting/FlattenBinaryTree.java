/**
 * Definition for binary tree
 * class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 * This solution uses a Queue. The solution that I used is a Stack. Available in FlattenTreeStack
 */
public class FlattenBinaryTree {
  public TreeNode flatten(TreeNode A) {
      
      Queue<TreeNode> queue = new LinkedList<TreeNode>();
      preorder(queue, A);
      
      if (queue.isEmpty())
          return A;
      
      TreeNode node = queue.remove();
      TreeNode next;
      A = node;
      
      while (!queue.isEmpty()) {
          next = queue.remove();
          node.left = null;
          node.right = next;
          next.left = null;
          node = next;
      }
      
      return A;
      
  }
  
  public void preorder(Queue<TreeNode> queue, TreeNode node) {
      
      if (node == null)
          return;
      
      queue.add(node);
      preorder(queue, node.left);
      preorder(queue, node.right);
      
  }
  
}
