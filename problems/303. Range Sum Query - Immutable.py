class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if len(nums) == 0:
            self.piled = []
        else:
            self.piled = nums[:]
            for i in range(1, len(nums)):
                self.piled[i] = self.piled[i - 1] + self.piled[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.piled[j]
        else:
            return self.piled[j] - self.piled[i - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)