class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lo = 0
        hi = len(nums) - 1
        k = 0
        while lo <= hi:
            nlo = nums[lo]
            nhi = nums[hi]
            if nums[lo] == val:
                nums[lo] = nhi
                hi -= 1
                k += 1
            else:
                lo += 1

        return len(nums) - k
