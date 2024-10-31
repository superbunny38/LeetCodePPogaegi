class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        left, right = 0, 0
        valid = 0
        min_len = float('inf')
        res = ""
        t_counter = Counter(t)
        window_counter = Counter()
        while right < m:
            right_char = s[right]
            if s[right] in t_counter:
                window_counter[right_char] += 1
                if t_counter[right_char] == window_counter[right_char]:
                    valid += 1
                while valid == len(t_counter):
                    left_char = s[left]
                    if right - left + 1 < min_len:
                        min_len = right - left + 1
                        res = s[left: right + 1]
                    if left_char in t_counter:
                        window_counter[left_char] -= 1
                        if window_counter[left_char] < t_counter[left_char]:
                            valid -= 1
                    left += 1
            right += 1
        return res
