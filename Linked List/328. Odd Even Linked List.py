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
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        oddDummy = ListNode(-1)
        oddcurr = oddDummy
        evenDummy = ListNode(-1)
        evencurr = evenDummy

        while head:
            oddcurr.next = head
            oddcurr = oddcurr.next
            head = head.next
            if head:
                evencurr.next = head
                head = head.next
                evencurr = evencurr.next
        evencurr.next = None

        oddcurr.next = evenDummy.next

        return oddDummy.next