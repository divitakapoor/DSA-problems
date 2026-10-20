class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        l=0
        sum=0
        minlength=float("inf")
        for r in range(n):
            sum=sum+nums[r]
            while sum>=target:
                minlength=min(minlength,r-l+1)
                sum=sum-nums[l]
                l+=1
        if minlength == float("inf"):
            return 0

        return minlength






        