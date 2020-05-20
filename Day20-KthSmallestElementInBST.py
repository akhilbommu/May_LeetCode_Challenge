"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class KthSmallestElementInBST:

    def __init__(self):
        self.inOrderList = []

    def inOrderTraversal(self, root):
        if not root:
            return self.inOrderList

        if root.left is not None:
            self.inOrderTraversal(root.left)

        self.inOrderList.append(root.val)

        if root.right is not None:
            self.inOrderTraversal(root.right)

        return self.inOrderList

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.inOrderTraversal(root)
        return self.inOrderList[k - 1]

