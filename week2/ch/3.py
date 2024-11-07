class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if s == "":
            return 0
        
        ㅣeft_idx = 0
        cur_char = ""
        max_length = -float('inf')
        for right_idx in range(len(s)):
            while s[right_idx] in cur_char:
                cur_char = cur_char[1:]
                ㅣeft_idx += 1
            cur_char += s[right_idx]
            cur_length = (right_idx-ㅣeft_idx+1)
            max_length = max(max_length,cur_length)
            right_idx += 1
        return max_length
