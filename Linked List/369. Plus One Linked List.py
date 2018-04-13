"""Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

"""

#有一种 Recursion的解法，用 DFS， 待研究

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tail = self.recurse(head)

        tail.val += 1

        curr = tail
        while curr.val == 10:
            curr.val = 0
            if curr.next:
                curr.next.val += 1
            else:
                curr.next = ListNode(1)
            curr = curr.next

        return self.recurse(tail)

    def recurse(self, head):
        prev = None
        while head:
            contp = head.next
            head.next = prev
            prev = head
            head = contp
        return prev
