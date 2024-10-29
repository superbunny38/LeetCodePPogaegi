class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            sums = numbers[left] + numbers[right]
            if sums == target:
                return [left + 1, right + 1]
            if sums < target:
                left += 1
            else:
                right -= 1
