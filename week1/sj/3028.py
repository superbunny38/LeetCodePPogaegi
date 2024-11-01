class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        pos = 0
        count = 0
        for num in nums:
            if num < 0:
                pos += num
            else:
                pos += num
            if pos == 0:
                count += 1
        return count
