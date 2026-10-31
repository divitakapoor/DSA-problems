class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mpp={}
        for i in nums:
            mpp[i]=mpp.get(i,0)+1
        for i in mpp:
            if mpp[i]==1:
                return i
        return -1
        