class Solution:
    def combinationSum(self, nums, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()

        def helper(nums,start,rem,list):
            if rem == 0:
                ans.append(list)
                return

            if rem < 0:
                return

            for i in range(start,len(nums)):
                if nums[i] > rem: return
                helper(nums,i,rem-nums[i],list+[nums[i]])

        helper(nums,0,target,[])
        return ans

print(Solution().combinationSum([2,3,5],8))