class Solution(object):
    def isAnagram(self, s, t):
        v=''.join(sorted(s))
        o=''.join(sorted(t))
        if v==o:
            return True
        else:
            return False
        