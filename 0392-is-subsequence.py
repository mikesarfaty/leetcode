class Solution:
    """
    O(s * len(t))
    """
    def isSubsequence(self, s: str, t: str) -> bool:

        def index_of_next(start, char):
            for ti in range(start, len(t)):
                if t[ti] == char:
                    return ti + 1
            return None

        ti = 0
        for char in s:
            ti = index_of_next(ti, char)
            if ti is None:
                return False

        return True
