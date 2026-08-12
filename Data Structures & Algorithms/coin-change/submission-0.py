class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
        
        return dp[amount] if dp[amount] != amount + 1 else -1
        

        # Example:
        # Amount = 7
        # [1, 3, 4, 5]

        # dp = [0, 1, 2, 1, 8, 8, 8, 8, 8]

        # and so on

        

        # NOTES:
        # set values equal to "max" base value so when we compare using min, it'll overrite it every time
        # min is used for when you go through a later coin that overrides the value set from a previous coin for that index
        # dp[0] = 0 is very important because we can get ex: dp[3-3] + 1 (if we have a 3 coin) it'll set that value to 1

