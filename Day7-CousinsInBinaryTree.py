"""
Problem Link : "https://leetcode.com/problems/cousins-in-binary-tree/"

Approach : Two nodes 'x' and 'y' are said to be cousins iff their value of depth is equal and they have
           different parents.
           Creating a dictionary object where the keys are values of each node in a tree
           and values are list conatining depth and value of its parent of that particular node.

           Example : root = [1,2,3,4] , x = 4, y = 3.
           Dictionary will now look as follows:
                                         {key : [values]}
                    {1: [0, None], 2: [1, 1], 4: [2, 2], 3: [1, 1]}

           After creating a dictionary object we check depth and parent values for 'x' and 'y' which we can
           access as "value[0]" and "value[1]" respectively.
           If both the conditions are satisfied we return True else False.
"""


class Solution:

    def __init__(self):
        self.lookup = dict()  # Creating an empty dictionary

    def addValuesToDict(self, root, i, parent_value):
        if root is None:  # if root is None we return
            return
        self.lookup[root.val] = [i, parent_value]  # adding keys and values to dictionary
        self.addValuesToDict(root.left, i + 1, root.val)  # recursive call on left sub-tree
        self.addValuesToDict(root.right, i + 1, root.val)  # recursive call on right sub-tree

    def isCousins(self, root, x: int, y: int) -> bool:
        self.addValuesToDict(root, 0, None)
        print(self.lookup)
        # checking for depth and parent values
        return self.lookup[x][0] == self.lookup[y][0] and self.lookup[x][1] != self.lookup[y][1]
