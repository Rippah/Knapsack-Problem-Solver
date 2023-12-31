def knapsack_dynamic(W, items):
    n = len(items)
    dp = [0] * (W + 1)

    for i in range(n):
        for w in range(W, items[i][0] - 1, -1):
            dp[w] = max(dp[w], items[i][1] + dp[w - items[i][0]])

    return dp[W]

items = [(2, 40), (3, 50), (2, 100), (5, 95), (3, 30)]
knapsack_capacity = 10

max_value_dynamic = knapsack_dynamic(knapsack_capacity, items)
print(f"Maximum value using dynamic programming: {max_value_dynamic}")