# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# The result could be none, so start with dummy
# Use slow and fast pointer to mark the difference

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        i = dummy
        j = dummy
        for M in range(n):
            j = j.next
        while j.next:
            i = i.next
            j = j.next

        i.next = i.next.next

        return dummy.next
