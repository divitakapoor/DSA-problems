class Solution:
    def rearrange(self,arr):
        # code here
       pos=[x for x in arr if x>=0]
       neg=[x for x in arr if x<0]
       ans=[]
       i=j=0
       while i<len(pos) and j<len(neg):
           ans.append(pos[i])
           ans.append(neg[j])
           i+=1
           j+=1
       ans.extend(pos[i:])
       ans.extend(neg[j:])
       arr[:]=ans
       return arr
