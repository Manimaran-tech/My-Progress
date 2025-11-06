class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        l=[]
        for i in nums:
            if i in l:
                l.remove(i)
            else:
                l.append(i)
        return l
