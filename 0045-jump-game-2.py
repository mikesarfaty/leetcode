class Solution:
    """
    dynamic programming look-ahead instead of check-behind
    """
    def jump(self, nums: List[int]) -> int:
        nn = len(nums)
        dp = [float("inf") for _ in range(nn)]
        dp[0] = 0
        for n in range(nn):
            for i in range(n + 1, n + nums[n] + 1):
                if i < nn:
                    dp[i] = min(dp[i], dp[n] + 1)

        return dp[-1]
