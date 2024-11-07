class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(sofar,comb,next_int):
            if sofar == k:
                ans.append(comb.copy())
                return
            else:
                for i in range(next_int,n+1):
                    comb.append(i)
                    backtrack(sofar+1,comb,i+1)
                    comb.pop(-1)
        
        backtrack(0,[],1)
        return ans
