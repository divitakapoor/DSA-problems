class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        maximum=max(arr)
        for i in range(len(arr)):
            if arr[i]==maximum:
                return i
        return -1

        