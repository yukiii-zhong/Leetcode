# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])


        n = len(nums)
        middle = int(n/2)
        node = TreeNode(nums[middle])
        node.left = self.sortedArrayToBST(nums[0:middle])
        node.right = self.sortedArrayToBST(nums[middle+1:n])

        return node
