class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        P = ""
        
        for i in range(len(s)):
            for j in range(len(s), i , -1):
                if( len(P) >= j-i):
                    break
                elif(s[i:j] == s[i:j][::-1]):
                    P = s[i:j]
                    break
        return P
                    
        
        