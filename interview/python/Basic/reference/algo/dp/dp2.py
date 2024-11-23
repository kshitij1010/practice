# 322. Coin Change
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.
# https://leetcode.com/problems/coin-change/
# Eg-1,
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Eg-2,
# Input: coins = [2], amount = 3
# Output: -1
# Eg-3,
# Input: coins = [1], amount = 0
# Output: 0
# Eg-4,
# Input: coins = [1], amount = 2
# Output: 2


def coinChange(self, coins, amount):
    dp = [0] * (amount)
    
    for a in range(amount+1):
        total = float('inf')
        for c in coins:
            if a-c >= 0:
                total = min(dp[a-c]+1, total)
        dp[a] = total
        
    if dp[-1] == float('inf'):
        return -1
    
    return dp[-1]
