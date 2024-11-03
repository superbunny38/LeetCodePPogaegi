class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        highest_freq_num = 0
        max_len = 0
        counter = defaultdict(int)
        while right < len(s):
            counter[s[right]] += 1
            while right - left + 1 - max(counter.values()) > k:
                counter[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len
