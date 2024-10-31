import heapq

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        hq = []
        bank_info = dict()
        for b in bank:
            bank_info[b] = defaultdict(int)

        #init bank info
        for b_idx in range(len(bank)):
            candidate = bank[b_idx]
            start_diffs = []
            for idx in range(8):
                if candidate[idx] != startGene[idx]:
                    start_diffs.append(idx)
            
            if len(start_diffs) == 1:
                heapq.heappush(hq,(1,candidate))
            
            
            for compare_idx in range(b_idx+1,len(bank)):
                compared_diffs = []
                to_compare_bank = bank[compare_idx]
                for idx in range(8):
                    if candidate[idx] != to_compare_bank[idx]:
                        compared_diffs.append(idx)
                
                if len(compared_diffs) == 1:
                    bank_info[to_compare_bank][candidate] = compared_diffs[0]
                    bank_info[candidate][to_compare_bank] = compared_diffs[0]
                    
        while hq:
            popped = heapq.heappop(hq)
            n_changed, curGene = popped[0],popped[1]
            # print(f"popped: n_changed:{n_changed} curGene:{curGene}")
            if curGene == endGene:
                return n_changed
            
            info = bank_info[curGene]
            # print("info:",info)
            for tryGene, diff_idx in info.items():
                if n_changed+1 > len(bank):
                    # print(f"{curGene}->{tryGene}: {n_changed+1}")
                    continue
                # print(f"push: ({n_changed+1},{tryGene})")
                heapq.heappush(hq,(n_changed+1,tryGene))

        return -1
