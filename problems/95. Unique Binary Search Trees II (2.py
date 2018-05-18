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

        def dfs(start,end):
            """
            :param start: int
            :param end: int
            :return: List[TreeNode]
            """
            res = []
            if start > end:
                return res

            if start == end:
                return [TreeNode(start)]

            for i in range(start,end+1):
                left = dfs(start,i-1)
                right = dfs(i+1, end)

                if len(left) > 0 and len(right) > 0:
                    for lnode in left:
                        for rnode in right:
                            root = TreeNode(i)
                            root.left = lnode
                            root.right = rnode
                            res.append(root)
                elif len(left) > 0 and len(right) == 0:
                    for lnode in left:
                        root = TreeNode(i)
                        root.left = lnode
                        res.append(root)
                elif len(right) > 0 and len(left) == 0:
                    for rnode in right:
                        root = TreeNode(i)
                        root.right = rnode
                        res.append(root)

            return res

        return dfs(1,n)


list = Solution().generateTrees(2)
for n in list:
    print(n)
