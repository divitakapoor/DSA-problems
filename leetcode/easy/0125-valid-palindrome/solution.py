class Solution:
    def isPalindrome(self, s):
        s=s.lower()
        result =''.join(i for i in s if i.isalnum())
        return result==result[::-1]  
        