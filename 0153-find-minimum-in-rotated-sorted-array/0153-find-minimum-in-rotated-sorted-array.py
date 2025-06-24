class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=nums[0]
        for i in nums:
            if low>i:
                low=i
        return low