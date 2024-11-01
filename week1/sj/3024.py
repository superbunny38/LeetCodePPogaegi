class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums[2] >= nums[0] + nums[1] or nums[1] >= nums[0] + nums[2] or nums[0] >= nums[1] + nums[2]:
            return "none"
        sets = set(nums)
        if len(sets) == 1:
            return "equilateral"
        elif len(sets) == 2:
            return "isosceles"
        else:
            return "scalene"
        
