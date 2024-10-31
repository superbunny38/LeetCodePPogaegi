class Solution:
    def get_newnum(self, n):
        res = 0
        while n:
            remain = n % 10
            n //= 10
            res += (remain * remain)
        return res

    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            n = self.get_newnum(n)
        
