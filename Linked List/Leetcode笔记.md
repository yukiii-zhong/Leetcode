# Leetcode Notes

## Linked List

###  234. Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

**Follow up:**
Could you do it in O(n) time and O(1) space?

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        
        middle = self.findMiddle(head)
        comp = self.reverse(middle.next)
        curr = head
        while comp:
            if curr.val != comp.val:
                return False
            curr = curr.next
            comp = comp.next
        return True
    
    def reverse(self, head):
        prev = None
        while head:
            # 用contp储存接下来的Node connection
            contp = head.next
            # 以head为基础，指向prev connections
            head.next = prev
            #接下来从head开始，都变成了prev
            prev = head
            # 开始下一轮
            head = contp
        return prev
    

    def findMiddle(self, head):
        # while the length is even number (6), comes to the 3rd node
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    
    
```

 

### 141. Linked List Cycle

> Given a linked list, determine if it has a cycle in it.
>
> Follow up:
> Can you solve it without using extra space?

#### 注意点：

"has a cycle" —> 不一定是从head开始

用fast, slow 指针寻找

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        
        slow = head
        fast = head.next
        
        while fast and fast.next:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next
            
        return False
```



