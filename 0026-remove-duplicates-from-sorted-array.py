class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lo = 0
        insert_at = 0
        lookahead = 1
        while lookahead < len(nums):
            nlo = nums[lo]
            nla = nums[lookahead]
            if nlo == nla:
                lookahead += 1
            else:
                nums[insert_at] = nlo
                lo = lookahead
                lookahead = lo + 1
                insert_at += 1

        nums[insert_at] = nums[lo]
        return insert_at + 1
