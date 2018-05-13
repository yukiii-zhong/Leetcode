class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = []
        items = []

        nums.sort()

        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                counts.append(1)
                items.append(nums[i])
            else:
                counts[-1] +=1

        ranks = counts[:]
        ranks.sort(reverse=True)
        ranks = ranks[:k]

        ans = []

        for i in range(len(counts)):
            if counts[i] in ranks:
                ans.append(items[i])

        return ans

    def topKFrequent2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        

test1 = Solution().topKFrequent([3,0,1,0],1)
print(test1)