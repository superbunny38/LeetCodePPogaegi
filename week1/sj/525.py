class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        hash_table = defaultdict(int)
        hash_table[0] = -1
        max_len = 0
        for i in range(n):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            if count in hash_table:
                max_len = max(max_len, i - hash_table[count])
            else:
                hash_table[count] = i
        return max_len
