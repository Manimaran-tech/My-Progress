class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d={}
        v=s.split()
        if len(pattern) != len(v):
            return False
        for i, j in zip(pattern, v):
            if i in d:
                if d[i] != j:
                    return False
            else:
                if j in d.values():
                    return False
                d[i] = j
        return True
