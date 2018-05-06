class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.store = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curMin = self.getMin()
        if curMin is None or x< curMin:
            self.store.append((x,x))
        else:
            self.store.append((x,curMin))


    def pop(self):
        """
        :rtype: void
        """
        self.store.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.store[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.store)==0:
            return None
        else:
            return self.store[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()