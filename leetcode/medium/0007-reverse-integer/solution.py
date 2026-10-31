class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            sign=-1
        else:
            sign =1
        x=str(abs(x))
        x=x[::-1]
        result=sign*int(x)
        if result>2**31 -1 or result<-2**31:
            return 0
        return result 