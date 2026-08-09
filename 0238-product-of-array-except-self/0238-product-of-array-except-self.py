class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res= [0] * n
        if len(nums) == 0: 
            return res
        
        prefix,suffix = [0]*n , [0]*n

        product = 1
        for i in range(n):
            product *= nums[i]
            prefix[i] = product

        product = 1
        for i in range(n-1,-1,-1):
            product *= nums[i]
            suffix[i] = product 

        res[0] = suffix[1]
        res[n-1] = prefix[n-2]

        for i in range(1,n-1):
            res[i] = prefix[i-1] * suffix[i+1]
        return res 
        