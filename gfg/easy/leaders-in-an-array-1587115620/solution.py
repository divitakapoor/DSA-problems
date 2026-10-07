class Solution:
    def leaders(self, arr):
        # code here
        leader=[]
        max_right=arr[-1]
        n=len(arr)
        leader.append(max_right)
        for i in range (n-2,-1,-1):
            if arr[i]>=max_right:
                leader.append(arr[i])
                max_right=arr[i]
        leader.reverse()
        return leader