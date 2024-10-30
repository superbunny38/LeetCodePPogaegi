
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        if len(citations) == 1:
            return min(1,citations[0])

        count = [0]*1001
        for citation in citations:
            count[citation] += 1

        max_n = -float('inf')
        max_count = 0
        for citation in citations:
            if sum(count[citation:])>=citation:
                max_n = max(max_n,citation)
        
        if max_count>0:
            return max_count
        else:
            for candi in range(len(citations),-1,-1):
                if sum(count[candi:])>=candi:
                    return candi
