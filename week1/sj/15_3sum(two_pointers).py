class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        for k in range(n - 2):
            # skipping duplicates for first element
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            target = -nums[k]
            left, right = k + 1, n - 1
            while left < right:
                sums = nums[left] + nums[right]
                if sums == target:
                    res.append([nums[k], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif sums < target:
                    left += 1
                else:
                    right -= 1
        return res
