class Solution:
    def reverse(self, x: int) -> int:
        a = 0
        flag = 1 if x > 0 else -1
        x = x if x > 0 else -x
        while (x != 0):
            a = a * 10 + x % 10
            x //= 10
        a *= flag
        if (a < -2**31) or (a > 2**31 + 1):
            a = 0
        return a
