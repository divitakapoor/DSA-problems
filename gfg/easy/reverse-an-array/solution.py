class Solution:
    def reverseArray(self, arr):
        # code here
        arr2=reversed(arr)
        arr[:]=arr2
        return arr
        
        