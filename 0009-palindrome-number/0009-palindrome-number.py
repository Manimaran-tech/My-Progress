class Solution(object):
    def isPalindrome(self, x):
        s=str(x)
        if s[::-1]==s:
            return True
        else:
            return False