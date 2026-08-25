class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = sell - buy
        # buy before sell
        # sell > buy

        l, r = 0, 1
        profit = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                current_profit = prices[r] - prices[l]
                profit = max(profit, current_profit)
            r += 1
        return profit