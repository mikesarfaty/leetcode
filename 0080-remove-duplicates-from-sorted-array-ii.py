class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = {}
        lookahead = 0
        insert_at = 0

        while lookahead < len(nums):
            nla = nums[lookahead]
            if nla not in seen:
                seen[nla] = 0

            if seen[nla] < 2:
                seen[nla] += 1
                nums[insert_at] = nla
                insert_at += 1
            
            lookahead += 1

        return insert_at
