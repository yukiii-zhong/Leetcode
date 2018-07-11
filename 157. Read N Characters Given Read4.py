# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        temp = ['' for _ in range(4)]
        total = 0

        while True:
            # Count how many chars can be read
            count = min(read4(temp), n)
            if count == 0: break

            # Update n
            n -= count

            # Store chars read before
            for i in range(count):
                buf[total] = temp[i]
                total += 1

        return total




