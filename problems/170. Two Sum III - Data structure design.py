class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        if number in self.table:
            self.table[number] += 1
        else:
            self.table[number] = 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num in self.table:
            if value - num == num:
                if self.table[num] > 1:
                    return True
            else:
                if value-num in self.table:
                    return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)