class Solution:
    """
    the longest_prefix has to be part of every word, start a possibility
    (the first string) and narrow it down on each iteration.
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = strs[0]

        for s in strs:
            while not s.startswith(longest_prefix):
                longest_prefix = longest_prefix[:-1]

        return longest_prefix
