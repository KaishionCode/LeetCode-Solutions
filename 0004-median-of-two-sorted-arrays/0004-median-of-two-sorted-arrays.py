class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if (len(nums1) > len(nums2)): nums1, nums2 = nums2, nums1
        m,n = len(nums1), len(nums2)
        vi_tri_giua = (m+n+1)//2
        left,right = 0,m
        while left <= right:
            nhom_A = (right + left) // 2
            nhom_B = vi_tri_giua - nhom_A
            
            maxleftA = float('-inf') if nhom_A == 0 else nums1[nhom_A-1]
            minrightA = float('inf') if nhom_A == m else nums1[nhom_A]

            maxleftB = float("-inf") if nhom_B == 0 else nums2[nhom_B - 1]
            minrightB= float("inf") if nhom_B == n else nums2[nhom_B]

            if maxleftA <= minrightB and maxleftB <= minrightA:
                if (m+n) % 2 == 1: return max(maxleftA,maxleftB)
                else: return (max(maxleftA,maxleftB) + min(minrightB,minrightA)) / 2.0
            elif maxleftA > minrightB: right = nhom_A - 1
            else: left = nhom_A + 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna