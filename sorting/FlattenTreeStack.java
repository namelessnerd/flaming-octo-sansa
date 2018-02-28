/**
 * Definition for binary tree
 * class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class FlattenTreeStack {
    static Stack<Integer> st = new Stack<Integer>();
	public TreeNode flatten(TreeNode a) {
	    if(a == null)
	        return a;
	    flattenSt(a);
	    a = null;

        while(!Solution.st.isEmpty())
        {
            TreeNode temp = new TreeNode(Solution.st.pop());
            if(a == null)
            {
                a = temp;
            }
            else
            {
                temp.right = a;
                a = temp;
            }
        }
        return a;
	}
	
	public void flattenSt(TreeNode a)
	{
	    if(a == null)
	        return;
	        
        Solution.st.push(a.val);
        flattenSt(a.left);
        flattenSt(a.right);
	}
}
