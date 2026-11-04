class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        fre={}
        count =0
        for i in stones:
            fre[i]=fre.get(i,0)+1
        for i in jewels:
            if i in fre:
                count =count+fre[i]
        return count 

        