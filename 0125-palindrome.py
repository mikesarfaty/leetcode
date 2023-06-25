class Solution:
    """
    2-pointer, skip/continue when non alphanumeric
    """
    def isPalindrome(self, s: str) -> bool:
        lo = 0
        hi = len(s) - 1
        while lo <= hi:
            if not s[lo].isalnum():
                lo += 1
            elif not s[hi].isalnum():
                hi -= 1
            else:
                if s[lo].lower() != s[hi].lower():
                    return False
                else:
                    lo += 1
                    hi -= 1

        return True
