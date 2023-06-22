class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) / 2
        frequencies = {}

        for n in nums:
            if n not in frequencies:
                frequencies[n] = 1
            else:
                frequencies[n] += 1
            
            if frequencies[n] > majority:
                return n
