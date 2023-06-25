class Solution:
    """
    ... didn't realize this one was a 2pointer problem
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nn = len(nums)
        nums.sort()
        r = []

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            j = i + 1
            k = nn - 1
            while j < k:
                if nums[j] + nums[k] == -n:
                    r.append((n, nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] > -n:
                    k -= 1
                else:
                    j += 1
        return list(set(r))
