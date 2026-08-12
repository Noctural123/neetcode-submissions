class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        min_price = prices[0]

        for price in prices:
            if price > min_price:
                maxP = max(maxP, price - min_price)
            elif price < min_price:
                min_price = price
        
        return maxP