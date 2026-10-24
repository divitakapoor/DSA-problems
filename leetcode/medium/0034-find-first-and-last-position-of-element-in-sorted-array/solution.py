class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findfirst():
            n=len(nums)
            low=0
            high=n-1
            ans=-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    ans=mid
                    high=mid-1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return ans
        def findlast():
            n=len(nums)
            low=0
            high=n-1
            ans=-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    ans=mid
                    low=mid+1
                elif nums[mid]<target:
                        low=mid+1
                else:
                        high=mid-1
            return ans
        return [findfirst(),findlast()]

        