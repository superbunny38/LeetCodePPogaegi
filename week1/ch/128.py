class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = set()
        max_count = 0
        for num in nums:
            hash.add(num)
        for num in nums:
            if num-1 in hash:
                continue
            find = num+1
            cur_count = 1
            while find in hash:
                cur_count+=1
                find +=1
            max_count = max(max_count,cur_count)
        return max_count
