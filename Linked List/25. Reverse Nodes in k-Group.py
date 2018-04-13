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
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        count = 0
        curr = head
        while curr and count < k:
            count +=1
            curr = curr.next
        if count ==k:
            curr = self.reverseKGroup(curr,k)
            for i in range(count):
                temp = head.next
                head.next = curr
                curr = head
                head = temp
            head = curr

        return head
