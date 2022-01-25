class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        ans = 0
        head = 0
        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]] = 1
            else:
                dict[s[i]] += 1

            if dict[s[i]] == 1:
                ans = max(ans, i - head + 1)
            else:
                while dict[s[i]] != 1:
                    dict[s[head]] -= 1
                    head += 1
        return ans
