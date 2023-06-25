class Solution:
    """
    Kind of like tokenization.
    """
    def lengthOfLastWord(self, s: str) -> int:
        reset = False
        r = 0
        for c in s:
            if c == " ":
                reset = True
            else:
                if reset:
                    r = 1
                    reset = False
                else: r += 1

        return r
