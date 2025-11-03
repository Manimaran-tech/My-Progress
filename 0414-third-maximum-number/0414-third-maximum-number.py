class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set(nums)               
        r = sorted(s, reverse=True) 
        if len(r) >= 3:
            return r[2]             
        else:
            return r[0]  
