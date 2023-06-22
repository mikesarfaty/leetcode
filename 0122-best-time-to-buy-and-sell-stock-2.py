class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.max_profit(prices, 0, {})

    def max_profit(self, prices, from_day, cache, own=False):
        """
        simple dynamic programming
        """
        if from_day == len(prices):
            return 0

        if (from_day, own,) in cache:
            return cache[(from_day, own,)]

        if not own:
            cache[(from_day, own,)] = max(
                self.max_profit(prices, from_day + 1, cache, own=True) - prices[from_day],
                self.max_profit(prices, from_day + 1, cache, own=False)
                )
        else:
            cache[(from_day, own,)] = max(
                self.max_profit(prices, from_day + 1, cache, own=False) + prices[from_day],
                self.max_profit(prices, from_day + 1, cache, own=True)
            )
        return cache[(from_day, own,)]
