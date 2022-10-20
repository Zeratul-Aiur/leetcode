class Solution:
    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        inf = 2**40
        m, n = len(nums1), len(nums2)
        if (m > n):
            return self.findMedianSortedArrays(nums2, nums1)
        left, right = 0, m
        maxleft, minright = 0, 0
        while left <= right:
            i = (left + right) // 2
            j = (n + m + 1) // 2 - i
            nums_im1 = (-inf if i == 0 else nums1[i - 1])
            nums_i = (inf if i == m else nums1[i])
            nums_jm1 = (-inf if j == 0 else nums2[j - 1])
            nums_j = (inf if j == n else nums2[j])

            if (nums_im1 <= nums_j):
                maxleft, minright = max(nums_im1,
                                        nums_jm1), min(nums_i, nums_j)
                left = i + 1
            else:
                right = i - 1
        return (maxleft + minright) / 2 if (m + n) % 2 == 0 else maxleft
