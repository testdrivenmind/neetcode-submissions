class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i = 1
        lowest_price = math.inf
        while i < len(prices):
            if prices[i] > prices[i-1]:
                lowest_price = min(lowest_price, prices[i-1])
                profit = prices[i] - lowest_price
                max_profit = max(profit, max_profit)
            i += 1
        return max_profit