class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, cur_min = 0, prices[0]
        for price in prices[1:]:
            max_profit = max(max_profit, price - cur_min)
            if price < cur_min:
                cur_min = price
        return max_profit
