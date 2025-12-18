class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        low, high = 0, n
        res = []

        for ch in s:
            if ch == 'I':
                res.append(low)
                low += 1
            else:  
                res.append(high)
                high -= 1

        res.append(low)  
        return res