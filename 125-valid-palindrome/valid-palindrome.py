class Solution:
    def isPalindrome(self, s):
        p = ""
        for c in s:
            if c.isalnum():
                p += c.lower()
        
        return p == p[::-1]