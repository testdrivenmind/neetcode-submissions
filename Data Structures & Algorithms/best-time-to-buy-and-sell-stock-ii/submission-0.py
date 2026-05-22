class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0 
        for day in range(1,len(prices)):
            if prices[day-1] > prices[day]:
                continue
            profit = prices[day] - prices[day-1]
            total_profit += profit
        return total_profit