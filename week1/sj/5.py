class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        max_len = 1
        max_substring = ""
        for i in range(n):
            if max_len == 1:
                max_substring = s[i]
            left, right = i - 1, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > max_len:
                    max_len = right - left + 1
                    max_substring = s[left: right + 1]
                left -= 1
                right += 1
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                if max_len < 2:
                    max_len = 2
                    max_substring = s[i:i + 2]
                left, right = i - 1, i + 2
                while left >= 0 and right < n and s[left] == s[right]:
                    if right - left + 1 > max_len:
                        max_len = right - left + 1
                        max_substring = s[left: right + 1]
                    left -= 1
                    right += 1
        return max_substring
        
