class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # find water can be trapped between 2 bars
        # i, j are 2 indexes
        def area(height, i, j):
            if j <= i + 1: return 0
            area = 0
            bar = min(height[i], height[j])
            for x in range(i + 1, j):
                area += (bar - height[x])
            return area

        # Find the highest bar and its index in given range
        # i included, j not included
        def max_Index(height, i, j):
            max = height[i]
            maxIndex = i
            for x in range(i, j):
                if height[x] > max:
                    max, maxIndex = height[x], x
            return maxIndex

        Hindex = max_Index(height, 0, len(height))

        sum = 0
        # Cal left trapped
        left = right = Hindex
        while left > 0:
            left = max_Index(height, 0, right)
            sum += area(height, left, right)
            right = left

        # Cal right trapped
        left = right = Hindex
        while right < len(height)-1:
            right = max_Index(height, left + 1, len(height))
            sum += area(height, left, right)
            left = right

        return sum


print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))