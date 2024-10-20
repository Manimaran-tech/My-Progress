class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l=sorted(nums1+nums2)
        if len(l)%2==0:
            v=int(len(l)/2)
            s=( l[v] + l[v-1])
            median = s/2
            return median
        else:
            v=int(len(l)/2)
            return l[v]