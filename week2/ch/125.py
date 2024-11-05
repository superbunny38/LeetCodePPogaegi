class Solution:
    def isPalindrome(self, s: str) -> bool:
        def convert(s):
            s = s.lower()
            s = s.replace(" ","")
            s = [_ for _ in s if _.isalnum()]
            return s
        s=convert(s)
        s_idx,e_idx = 0,len(s)-1
        while True:
            if s_idx>e_idx:
                return True
            elif s_idx == e_idx:
                return True
            if s[s_idx] == s[e_idx]:
                s_idx+=1
                e_idx-=1
            else:
                return False
