class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        
        def backtrack(combi, cur_sum,next_val_idx):
            if cur_sum == target:
               ans.append(combi.copy()) 
            
            for i in range(next_val_idx,len(candidates)):
                if cur_sum + candidates[i] > target:
                    continue
                backtrack(combi + [candidates[i]], cur_sum + candidates[i],i)

        backtrack([], 0,0)
        return ans
