import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = []
        for num in nums:
            heapq.heappush(hq,-num)
        for _ in range(k):
            popped = -heapq.heappop(hq)
        return popped
