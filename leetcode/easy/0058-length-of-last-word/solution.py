class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ss=s.split()
        length=len(ss[-1])
        return length
        
        