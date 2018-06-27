# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder and not postorder: return None
        rootVal = postorder[-1]
        leftnumber = inorder.index(rootVal)
        root = TreeNode(rootVal)
        root.left = self.buildTree(inorder[:leftnumber],postorder[:leftnumber])
        root.right = self.buildTree(inorder[leftnumber+1:],postorder[leftnumber:-1])
        return root