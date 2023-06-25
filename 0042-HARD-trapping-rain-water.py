class Solution:
    def trap(self, height: List[int]) -> int:
        nn = len(height)
        maxls = [0 for _ in range(nn)]

        new_max = 0
        for i in range(nn):
            maxls[i] = new_max
            new_max = max(height[i], new_max)

        max_right = 0
        trapable = 0
        for i in range(nn -1, -1, -1):
            if height[i] < min(maxls[i], max_right):
                trapable += min(maxls[i], max_right) - height[i]
            max_right = max(height[i], max_right)

        return trapable

