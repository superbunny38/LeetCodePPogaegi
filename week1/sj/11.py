class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        max_water = 0
        while left < right:
            water = min(height[left], height[right]) * (right - left)
            max_water = max(max_water, water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water
