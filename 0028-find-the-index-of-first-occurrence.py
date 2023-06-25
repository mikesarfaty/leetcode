class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nn = len(needle)
        hh = len(haystack)
        
        def check_from(start):
            for i, char in enumerate(needle):
                if haystack[start + i] != char:
                    return False
            
            return True
    
        for i in range(hh - nn + 1):
            if check_from(i):
                return i

        return -1
