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
    def __init__(self):
        self. a = 1

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Count length
        len1 = self.length(l1)
        len2 = self.length(l2)

        # add Empty location
        if len1 > len2:
            l2 = self.addEmpty(l2, len1 - len2)
        elif len2 > len1:
            l1 = self.addEmpty(l1, len2 - len1)

        # Plus
        dummy = ListNode(0)
        dummy.next = l2
        pre = dummy
        mark = dummy

        while l1 and l2:
            l2.val = l1.val + l2.val

            if l2.val >= 10:
                pre.val += 1
                l2.val -= 10

                # if pre== 10, means beforehead pre == 9, also means mark is before pre
                if pre.val == 10:
                    mark.val += 1
                    while mark.next != l2:
                        mark.next.val = 0
                        mark = mark.next

                mark = l2
            elif l2.val < 9:
                mark = l2

            l2 = l2.next
            l1 = l1.next
            pre = pre.next

        if dummy.val == 0:
            return dummy.next
        elif dummy.val == 1:
            return dummy

    def addEmpty(self, head, k):
        """
        for i in range(k):
            a = ListNode(0)
            a.next = head
            head = a
        return head
        """

        #Recursion way
        if k == 0:
            return head
        a = ListNode(0)
        a.next = head
        return self.addEmpty(a, k-1)


    def length(self, head):
        ans = 0
        while head:
            ans += 1
            head = head.next
        return ans


L1 = ListNode(1)
L1 = L1.newValue([9])
L2 = ListNode(1)
L2 = L2.newValue([9,9,9])

S1 = Solution()
print(S1.addTwoNumbers(L1,L2))


