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
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        curr = head
        head = head.next

        while head:


            if head.val < curr.val:
                temp = head.next
                pre = dummy

                while head.val >= pre.next.val:
                    pre = pre.next

                head.next = pre.next
                pre.next = head
                curr.next = temp
                head = temp
            else:
                head = head.next
                curr = curr.next

        return dummy.next

# Test
L1 = ListNode(1)
L1 = L1.newValue([3,2,1])
S1 = Solution()
print(S1.insertionSortList(L1))