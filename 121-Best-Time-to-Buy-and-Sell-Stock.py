class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # First Sol time: o(n), space: o(1)
        max_profit, ptr_buy, ptr_sell = 0, 0, 1

        if len(prices) == 0:
            return max_profit

        while (ptr_sell < len(prices)):
            if prices[ptr_buy] > prices[ptr_sell]:
                ptr_buy = ptr_sell
                ptr_sell += 1
                continue
            
            max_profit = max(max_profit, (prices[ptr_sell] - prices[ptr_buy]))
            ptr_sell += 1
        
        return max_profit

        