class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set(nums)
        count =0
        longest=0
        for i in s:
            if i-1 not in s :
                count =1
                while i+1 in s:
                    i+=1
                    count+=1
                longest=max(longest,count)
        return longest
        