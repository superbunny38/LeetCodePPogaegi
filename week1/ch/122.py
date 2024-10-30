class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = False
        hold_n = float('inf')
        profit = 0
        for idx in range(len(prices)-1):
            if prices[idx]<prices[idx+1]:
                if hold:
                    hold_n = min(hold_n,prices[idx])
                else:
                    hold_n = prices[idx]
                    hold = True

            elif prices[idx]>prices[idx+1]:
                if hold:
                    profit += max(0,prices[idx]-hold_n)
                    print("+:",prices[idx]-hold_n)
                    hold = False
                    hold_n = 0
        if hold:
            return max(profit,profit+(prices[idx+1]-hold_n))
        return profit
