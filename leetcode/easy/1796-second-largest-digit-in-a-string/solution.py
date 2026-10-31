class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        largest=-1
        second=-1
        for i in s:
            if i.isdigit():
                num=int(i)
                if num>largest:
                    second=largest
                    largest=num
                elif num<largest and num>second:
                    second=num
        return second

