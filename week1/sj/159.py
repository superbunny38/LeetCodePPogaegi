class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left, right = 0, 0
        max_len = 0
        counter = defaultdict(int)
        while right < len(s):
            counter[s[right]] += 1
            while left <= right and len(counter) > 2:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len
            
