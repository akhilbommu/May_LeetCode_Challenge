""""
Problem Link : "https://leetcode.com/problems/odd-even-linked-list/"
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        odd_node = head
        even_node = head.next
        odd_head = head
        even_head = head.next
        while even_node is not None and even_node.next is not None:
            odd_node.next = odd_node.next.next
            even_node.next = even_node.next.next
            even_node = even_node.next
            odd_node = odd_node.next
        odd_node.next = even_head
        return odd_head

