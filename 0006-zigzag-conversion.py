class Solution:
    """
    bouncing b/w rows, changing directions when hitting
    the top or bottom row
    """
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = ["" for _ in range(numRows)]
        direction = 1
        r = 0
        for i, c in enumerate(s):
            rows[r] += c
            if r == 0:
                direction = 1
            elif r == numRows - 1:
                direction = -1
            r += direction

        return "".join(rows)
