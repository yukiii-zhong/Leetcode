class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        for i in range(len(gas)):
            gas[i] -= cost[i]

        i = 0
        while i < len(gas):
            if gas[i] < 0:
                i += 1
            else:
                start = i
                temp = 0
                while True:
                    temp += gas[i]
                    if i == len(gas) - 1:
                        i = 0
                    else:
                        i += 1
                    if temp<0:
                        if i<=start:
                            return -1
                        else:
                            break
                    if i == start:
                        return start
        return -1

print(Solution().canCompleteCircuit(gas  = [1,2,3,4,5], cost = [3,4,5,1,2]))