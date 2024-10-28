class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0 for _ in range(n + 1)]
        hashmap = defaultdict(int)
        hashmap[0] += 1
        count = 0

        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
            count += hashmap[prefix_sum[i] - k]
            hashmap[prefix_sum[i]] += 1

        return count
