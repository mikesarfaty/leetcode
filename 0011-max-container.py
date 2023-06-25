class Solution:
    """
    2-pointer
    """
    def maxArea(self, height: List[int]) -> int:
        lo = 0
        hi = len(height) - 1

        max_container = float("-inf")

        while lo < hi:
            hlo = height[lo]
            hhi = height[hi]
            this_container = min(hlo, hhi) * (hi - lo)
            max_container = max(max_container, this_container)
            if hlo < hhi:
                lo += 1
            else:
                hi -= 1

        return max_container

