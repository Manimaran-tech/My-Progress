class Solution(object):
    def twoSum(self, numbers, target):
        d={}
        for i in range(len(numbers)):
            search=target - numbers[i]
            if search in d:
                return [d[search]+1,i+1]
            d[numbers[i]]=i

       
        