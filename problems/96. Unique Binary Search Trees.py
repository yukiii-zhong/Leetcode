class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(n,seen):
            # seen: {n: 个数}
            if n in seen: return seen[n]

            ans = 0
            for i in range(1,n+1):
                # how many possible ans for left and right branch
                # Store possible ans
                left = helper(i-1,seen)
                seen[i-1] = left
                right = helper(n-i,seen)
                seen[n-i] = right

                if left ==0 or right == 0:
                    temp = left + right
                else:
                    temp = left * right

                ans += temp

            return ans


        return helper(n, {0:0, 1:1})

    def numTrees2(self, n):
        nums = [0] * (n+1)
        nums[0] = 1
        nums[1] = 1

        for i in range(2,n+1):
            for j in range(1,i+1):
                nums[i] += nums[j-1] * nums[i-j]
        return nums[n]


print(Solution().numTrees2(3))