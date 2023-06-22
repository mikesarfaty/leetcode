class Solution:
    """
    DFS

    Also did dp
    """
    def canJump(self, nums: List[int]) -> bool:
        stack = [0]
        seen = set([])
        while stack:
            this = stack.pop(-1)
            if this in seen:
                continue
            else:
                seen.add(this)

            if this >= len(nums) - 1:
                return True
            else:
                for i in range(this + 1, this + nums[this] + 1):
                    if i not in seen:
                        stack.append(i)

        return False

