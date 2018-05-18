# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        res = "[" + str(self.val) + ", "
        if self.left:
            res += str(self.left.val)
        else:
            res += "Null"
        res += ", "
        if self.right:
            res += str(self.right.val)
        else:
            res += "Null"

        res += "]"

        return res



class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        A = [[]] * (n+1)
        for i in range(n+1):
            if i == 0:
                A[i] = []
            elif i ==1:
                A[i] = [TreeNode(1)]
            else:
                for j in range(1,i+1):
                    left = A[j-1]
                    right = A[i-j]

                    if left != [] and right != []:
                        for left_temp in left:
                            for right_temp in right:
                                temp = TreeNode(j)
                                temp.left = left_temp
                                temp.right = self.changeTreeValue(right_temp,j)
                                A[i].append(temp)

                    elif left != [] and right == []:
                        for left_temp in left:
                            temp = TreeNode(j)
                            temp.left = left_temp
                            A[i].append(temp)

                    elif right != [] and left == []:
                        for right_temp in right:
                            temp = TreeNode(j)
                            temp.right = self.changeTreeValue(right_temp, j)
                            A[i].append(temp)

        return A[2]


    def changeTreeValue(self,node,change):
        """
        :param head: TreeNode
        :param change: int
        :return: None
        """
        copy = TreeNode(node.val+change)

        if node.left:
            copy.left = self.changeTreeValue(node.left,change)

        if node.right:
            copy.right = self.changeTreeValue(node.right,change)

        return copy

N1 = TreeNode(0)
N1.left = TreeNode(-9)
N1.right = TreeNode(9)
N2 = Solution().changeTreeValue(N1,3)
N1.right.right= N2
N1.right.left = N2
print(Solution().changeTreeValue(N1,1).right)

