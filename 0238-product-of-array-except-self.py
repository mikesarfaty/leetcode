class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nn = len(nums)
        product_at = [nums[i] for i in range(nn)]
        product_after = [1 for i in range(nn)]
        res = []

        for i in range(1, nn):
            n = nums[i]
            product_at[i] = product_at[i - 1] * n

        for i in range(nn - 2, -1, -1):
            product_after[i] = product_after[i + 1] * nums[i + 1]

        res = [product_after[0]]
        for i in range(1, nn):
            res.append(product_at[i - 1] * product_after[i])

        return res
