class Solution(object):
    def lengthOfLastWord(self, s):
        v=s.strip().split()
        return len(v[-1])
        