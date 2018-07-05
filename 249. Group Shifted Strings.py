class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        if not strings: return []

        # table: {'abc': ['abc','bcd','xyz']}
        table = {}

        for str in strings:
            # find origin
            origin = ''
            gap = ord(str[0]) - ord('a')
            for char in str:
                newOrd = ord(char) - gap
                if newOrd < ord('a'):
                    newOrd += 26
                origin += chr(newOrd)

            # store origin
            if origin in table:
                table[origin].append(str)
            else:
                table[origin] = [str]

        return table.values()