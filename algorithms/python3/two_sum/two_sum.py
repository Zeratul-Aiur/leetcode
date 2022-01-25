class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newline = [[nums[i], i] for i in range(len(nums))]
        newline.sort()
        for i in range(len(newline)):
            head = 0
            tail = len(newline) - 1
            while head <= tail:
                mid = (head + tail) // 2
                if mid != i and newline[mid][0] + newline[i][0] == target:
                    return [newline[mid][1], newline[i][1]]
                elif newline[mid][0] + newline[i][0] < target:
                    head = mid + 1
                else:
                    tail = mid - 1
