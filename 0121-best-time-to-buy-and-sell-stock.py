class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prevmin = None
        maxp = 0

        for p in prices:
            if prevmin is None:
                prevmin = p
            else:
                maxp = max(maxp, p - prevmin)
                prevmin = min(prevmin, p)

        return maxp
