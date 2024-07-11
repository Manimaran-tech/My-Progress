class Solution(object):
    def groupAnagrams(self, strs):
        d={}
        for i in strs:
            v=''.join(sorted(i))
            if v not in d:
                d[v]=[]
            d[v].append(i)
        return list(d.values())
        