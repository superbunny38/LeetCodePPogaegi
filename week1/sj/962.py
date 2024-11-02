class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        max_width = 0
        for i in range(len(nums)):
            if not stack or nums[stack[-1]] >= nums[i]:
                stack.append(i)
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                max_width = max(max_width, j - stack[-1])
                stack.pop()
        return max_width
