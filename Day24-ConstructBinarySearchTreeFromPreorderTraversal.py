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
