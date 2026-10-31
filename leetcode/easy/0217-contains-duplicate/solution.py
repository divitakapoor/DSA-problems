class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mpp={}
        for i in nums:
            mpp[i]=mpp.get(i,0)+1
        for i in mpp:
            if mpp[i] >1:
                return True
        return False        