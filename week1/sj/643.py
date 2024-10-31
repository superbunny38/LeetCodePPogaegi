class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums = sum(nums[:k])
        max_sum = sums
        for i in range(k, len(nums), 1):
            sums += (nums[i] - nums[i - k])
            max_sum = max(max_sum, sums)
        return max_sum / k
