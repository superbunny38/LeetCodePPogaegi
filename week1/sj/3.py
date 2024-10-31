class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left, right = 0, 0
        cur_list = ""
        max_len = 0
        while right < len(s):
            if s[right] not in cur_list:
                cur_list += s[right]
                max_len = max(max_len, right - left + 1)
            else:
                while left < right and s[left] != s[right]:
                    left += 1
                left += 1
                cur_list = s[left:right + 1]
            right += 1
        return max_len
