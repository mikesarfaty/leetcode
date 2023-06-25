class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = len(s)
        if not ss:
            return 0

        start = 0
        end = 0
        seen = {}
        max_substr_len = float("-inf")

        while end < ss:
            c_end = s[end]
            if c_end in seen:
                for i in range(start, seen[c_end]):
                    del seen[s[i]]
                start = seen[c_end] + 1
                seen[c_end] = end
                end += 1
            else:
                seen[s[end]] = end
                end += 1
                max_substr_len = max(max_substr_len, end - start)

        return max_substr_len

