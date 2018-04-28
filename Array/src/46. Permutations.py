class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        self.res = []
        n = len(nums)


        def helper(n, nums, list):

            if (len(list) == n):
                self.res.append(list)
                return

            for num in nums:
                num_copy = nums[:]
                num_copy.remove(num)
                helper(n, num_copy, list + [num])

        helper(n,nums,[])

        return self.res


