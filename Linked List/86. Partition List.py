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
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        count = 0
        pre = dummy

        while head:
            count +=1
            temp = head.next
            if count == m:
                mNode = head
            if count < m:
                pre = pre.next
            if count > m and count <= n:
                head.next = pre.next
                pre.next = head
                mNode.next = temp
            head = temp
        return dummy.next


L1 = ListNode(1)
L1 = L1.newValue([1,2,3,4])
S1 = Solution()

print(S1.reverseBetween(L1,1,4))