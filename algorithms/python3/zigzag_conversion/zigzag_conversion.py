class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows == 1):
            return s
        array = [[0 for i in range(len(s))] for j in range(numRows)]
        x, y = -1, 0
        dx, dy = 1, 0
        result = ""
        for i in range(len(s)):
            x += dx
            y += dy
            array[x][y] = s[i]
            if (x == numRows - 1):
                dx, dy = -1, 1
            elif (x == 0 and dx == -1):
                dx, dy = 1, 0
        for i in range(numRows):
            for j in range(len(s)):
                if (array[i][j] != 0):
                    result = result + array[i][j]
        return result
