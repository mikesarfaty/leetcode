class Solution:
    """
    horrible :/
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        nn = len(nums)
        start = 0
        end = 0
        cursum = 0
        min_size = float("+inf")

        while end < nn:
            cursum += nums[end]

            while cursum >= target:
                min_size = min(min_size, end - start + 1)
                cursum -= nums[start]
                start += 1

            end += 1


        if min_size > nn:
            return 0
        else:
            return min_size
