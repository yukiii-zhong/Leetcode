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
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        pre = dummy = ListNode("#")
        pre.next = head
        slow = head
        fast = head
        while fast and fast.next:
            pre = pre.next
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        trav = self.traverse(slow)

        while head and trav:
            headTemp = head.next
            head.next = trav
            travTemp = trav.next
            pre = trav
            trav.next = headTemp
            head = headTemp
            trav = travTemp

        if trav:
            pre.next = trav

        return dummy.next


    def traverse(self,head):
        pre = None
        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre


    def __init__(self):
        self. a = 1

L1 = ListNode(1)
#L1 = L1.newValue([1,2,3,4,5])
S1 = Solution()
print(S1.reorderList(L1))