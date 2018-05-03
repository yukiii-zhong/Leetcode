class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag2 = list(magazine)

        for char in ransomNote:
            if char in mag2:
                mag2.remove(char)
            else:
                return False

        return True

    def canConstruct2(self, ransomNote, magazine):

        for char in set(ransomNote):
            if ransomNote.count(char) > magazine.count[char]:
                return False
        return True

a = [1,1,2,2,3,4]
b = set(a)
print(b)