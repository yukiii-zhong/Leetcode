class Solution:

    # dfs
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        def dfs (start,end):

            # int(float) method, 去小数点后面的数
            mid = int((start + end)/2)

            if mid **2 > x:
                return dfs(start,mid-1)
            else:
                if (mid+1) ** 2 > x:
                    return mid
                else:
                    return dfs(mid+1,end)

        return dfs(0,x)

    # 算法相同，用While
    def mySqrt2(self, x):

        if x == 0: return 0

        start, end = 0, x

        while True:
            mid = int((start+end)/2)

            if mid **2 > x:
                end = mid - 1
            else:
                if (mid+1) ** 2 > x:
                    return mid
                else:
                    start = mid +1


import math


print( round(2.333334,0))
print(Solution().mySqrt(4))