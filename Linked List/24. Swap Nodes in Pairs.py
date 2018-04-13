# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):

        ans = ""
        curr = self
        while curr:
            ans += str(curr.val) + " -> "
            curr = curr.next
        return ans[:-4]

    def newValue(self, inputList):

        pre = self
        for i in inputList:
            pre.next = ListNode(i)
            pre = pre.next
        return self.next

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # if head and !head.next
        pre = head

        if head and head.next:
            pre = head.next
            head.next = self.swapPairs(pre.next)
            pre.next = head

        return pre




    def swapPairs2_SLOW(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(-1)
        curr = dummy

        while head and head.next:
            pre = head
            curr.next = head.next
            head = head.next.next
            curr.next.next = pre
            curr = curr.next.next

        if head:
            curr.next = head
        else:
            curr.next = None

        return dummy.next