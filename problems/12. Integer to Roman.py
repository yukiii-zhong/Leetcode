class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ""
        dic = [['I','V'],['X','L'],['C','D'],['M']]
        i = 0
        while num > 0:
            dig, num = num %10, num // 10
            if dig <=3:
                res = dic[i][0]*dig + res
            elif dig == 4:
                res = dic[i][0]+dic[i][1] + res
            elif dig >=5 and dig <=8:
                res = dic[i][1]+ dic[i][0]*(dig-5) + res
            elif dig == 9:
                res = dic[i][0] + dic[i+1][0] + res
            i+=1
        return res

print(Solution().intToRoman(3999))