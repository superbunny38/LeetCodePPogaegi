class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]
        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(num)
            else:
                index = bisect_left(sub, num)
                sub[index] = num
        return len(sub)
