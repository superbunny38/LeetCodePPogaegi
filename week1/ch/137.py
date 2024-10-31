from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        storage = defaultdict(int)
        for num in nums:
            storage[num] += 1
            if storage[num] == 3:
                del storage[num]
        return list(storage.keys())[0]
