class Solution:
    def threeSumClosest(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = nums[0]+nums[1]+nums[2]
        for a in range(len(nums)-2):
            i=a+1
            j=len(nums)-1

            while j>i:
                sum = nums[a] + nums[i] + nums[j]
                if sum == target:
                    return sum
                if abs(closest-target)>abs(sum-target):
                    closest = sum

                if sum < target:
                    i +=1
                else:
                    j -= 1

        return closest

nums = [-3,-2,-5,3,-4]
print(Solution().threeSumClosest(nums,-1))