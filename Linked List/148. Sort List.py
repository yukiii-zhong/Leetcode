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

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        middle = self.findMiddle(head)
        next = middle.next
        middle.next = None
        return self.merge(self.sortList(head),self.sortList(next))

    def findMiddle(self,head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Merge 2 sorted List
    def merge(self,l1, l2):
        pre = dummy = ListNode(0)

        while l1 and l2:
            if l1.val >= l2.val:
                pre.next = l2
                l2 = l2.next
            else:
                pre.next = l1
                l1 = l1.next
            pre = pre.next

        if l1 == None:
            pre.next = l2
        else:
            pre.next = l1

        return dummy.next

    def __init__(self):
        self. a = 1

L1 = ListNode(1)
L1 = L1.newValue([2,9,1])
S1 = Solution()
print(S1.sortList(L1))