class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        mpp={}
        for i in nums:
            mpp[i]=mpp.get(i,0)+1
        while mpp:
          for x in sorted(mpp):
            ans.append(x)
            mpp[x]-=1
          for x in list(mpp):
            if mpp[x]==0:
                del mpp[x]
        return ans
