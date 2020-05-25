"""
Problem Link : "https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/"
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder) -> TreeNode:
        if len(preorder) == 0:
            return None
        root_node = TreeNode(preorder[0])
        index = 1
        while index < len(preorder) and preorder[index] < root_node.val:
            index += 1
        root_node.left = self.bstFromPreorder(preorder[1:index])
        root_node.right = self.bstFromPreorder(preorder[index:])
        return root_node


"""
Java Solution : 
--------------

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode bstFromPreorder(int[] preorder) {
        return constructBST(preorder,0,preorder.length-1);
    }
    public TreeNode constructBST(int[] preorder,int start,int end){
        if(start > end){
            return null;
        }
        TreeNode root = new TreeNode(preorder[start]);
        int i;
        for(i=start;i<=end;i++){
            if(preorder[i] > root.val){
                break;
            }
        }
        root.left = constructBST(preorder,start+1,i-1);
        root.right = constructBST(preorder,i,end);
        return root;
    }
}
"""