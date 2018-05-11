# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder)== 0: return None


        x = inorder.index(preorder[0])

        root = TreeNode(preorder[0])

        root.left = self.buildTree(preorder[1:x+1], inorder[0:x])

        root.right = self.buildTree(preorder[x+1:],inorder[x+1:])

        return root