# Knapsack Problem | DP
#
# Given weights and values of n items,
# put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
# In other words, given two integer arrays val[0..n-1] and wt[0..n-1]
# which represent values and weights associated with n items respectively.
# Also given an integer W which represents knapsack capacity,
# find out the maximum value subset of val[]
# such that sum of the weights of this subset is smaller than or equal to W.
# You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).
#
# Reference:
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/


def knapsack(knapsack_dict, WT):
    weights = []
    prices = []

    for w, p in knapsack_dict.items():
        weights.append(w)
        prices.append(p)

    return find_knapsack(weights, prices, WT)


def find_knapsack(weights, prices, WT):
    K = [ [0]*(WT+1) for _ in range(len(weights)+1)]

    for i in range(1, len(weights)+1):
        for w in range(1, WT+1):
            if w < weights[i-1]:
                K[i][w] = K[i-1][w]
            else:
                K[i][w] = max(K[i-1][w], prices[i-1] + K[i-1][w-weights[i-1]])

    return K[-1][-1]


knapsack_dict = {
                    2: 50,
                    5: 30,
                    7: 70
                }
print (knapsack(knapsack_dict, 4)) # 50

k_weight = [6, 2, 1]
k_price = [40, 20, 50]
print (find_knapsack(k_weight, k_price, 8)) # 90


k_weight = [10, 20, 30]
k_price = [60, 100, 120]
print (find_knapsack(k_weight, k_price, 50)) # 220
