class Solution:
    """
    lookahead
    """
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        res = 0
        idx = 0
        while idx < len(s):
            if idx < len(s) - 1 and values[s[idx]] < values[s[idx + 1]]:
                res += values[s[idx + 1]] - values[s[idx]]
                idx += 2
            else:
                res += values[s[idx]]
                idx += 1

        return res
