class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash = [0] * 128 
        for ch in s:
            hash[ord(ch)] += 1
        res = 0
        flag = False
        for count in hash:
            if count % 2 == 0:
                res+=count
            else:
                res+=(count-1)
                flag = True
        if flag:
            return res+1
        return res