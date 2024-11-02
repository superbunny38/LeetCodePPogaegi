class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1:
            return []
        res = []
        i = 2
        remains = finalSum
        while i <= remains:
            res.append(i)
            remains -= i
            i += 2
        if remains:
            res[-1] += remains
        return res
