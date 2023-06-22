class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        n = len(nums)
        nums[:] = nums[n - k:] + nums[:n - k]

        """
        I disagree with the premise of this question; without a pen and paper,
        the reversal pattern is unrecognizable to see to complete in O(1) space.

        So instead, language pointer hack.
        """
