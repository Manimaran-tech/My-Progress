class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=0
        j=0
        l=[]
        while i<len(nums1) and j < len(nums2):
            if nums1[i]<nums2[j]:
                l.append(nums1[i])
                i=i+1
            else:
                l.append(nums2[j])
                j=j+1
        l.extend(nums1[i:])
        l.extend(nums2[j:])
        n = len(l)
        if n % 2 != 0:
            return l[n // 2]
        else:
            return (l[n // 2 - 1] + l[n // 2]) / 2.0
