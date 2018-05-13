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
        # mapping: [[num, count], [], []]
        mapping = []
        maxcount = 0
        nums.sort()

        for i in range(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                mapping.append([nums[i],1])
            else:
                mapping[-1][1] +=1

            maxcount = max(maxcount,mapping[-1][1])

        mapping.sort(key=lambda x: x[-1])

        ans = []
        for i in range(k):
            ans.append(mapping[-1][0])
            mapping.pop()

        return ans

    def topKFrequent3(self, nums, k):

        mapping = {}

        for num in nums:
            if num in mapping:
                mapping[num] +=1
            else:
                mapping[num] = 1

        rank = sorted(mapping.items(), key= lambda item: item[-1])

        ans = []
        for i in range(k):
            ans.append(rank[-1][0])
            rank.pop()

        return ans

test1 = Solution().topKFrequent3([3,3,3,3,0,1,0],2)
print(test1)