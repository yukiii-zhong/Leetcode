class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # n is each integer in

        def helper(nums, start, end):
            # start, end: 值的范围

            if start == end: return start

            # count how many num in [start,mid]
            count = 0
            mid = (start + end) // 2
            for num in nums:
                if num >= start and num <= mid:
                    count += 1

            if count <= mid - start + 1:
                return helper(nums, mid + 1, end)
            else:
                return helper(nums, start, mid)

        return helper(nums, 1, len(nums) - 1)