class Solution:
    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        def findKth(K):
            indexa, indexb = 0, 0
            while (True):
                if (indexa == m):
                    return nums2[indexb + K - 1]
                if (indexb == n):
                    return nums1[indexa + K - 1]
                if (K == 1):
                    return min(nums1[indexa], nums2[indexb])

                newindexa = min(indexa + K // 2 - 1, m - 1)
                newindexb = min(indexb + K // 2 - 1, n - 1)
                if (nums1[newindexa] <= nums2[newindexb]):
                    K -= newindexa - indexa + 1
                    indexa = newindexa + 1
                else:
                    K -= newindexb - indexb + 1
                    indexb = newindexb + 1

        m, n = len(nums1), len(nums2)
        total = m + n
        if (total % 2 == 1):
            return findKth(total // 2 + 1)
        return (findKth(total // 2) + findKth(total // 2 + 1)) / 2
