import sys
sys.setrecursionlimit(10**6)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def solve(number,power):
            if power == 0:
                return 1
            elif power%2 == 1:
                return number*(solve(number*number,int((power-1)/2)))
            else:
                return solve(number*number,int(power/2))
    
        if n == 0:
            return 1
        elif n<0:
            return 1/solve(x,abs(n))
        else:
            return solve(x,abs(n))
