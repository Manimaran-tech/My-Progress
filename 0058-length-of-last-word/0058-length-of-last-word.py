class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        v= s.split()
        return len(v[-1])