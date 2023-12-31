def knapsack_naive(W, items, n):
    if n == 0 or W == 0:
        return 0

    if items[n - 1][0] > W:
        return knapsack_naive(W, items, n - 1)

    else:
        include_item = items[n - 1][1] + knapsack_naive(W - items[n - 1][0], items, n - 1)
        exclude_item = knapsack_naive(W, items, n - 1)
        return max(include_item, exclude_item)

# Example usage:
items = [(2, 40), (3, 50), (2, 100), (5, 95), (3, 30)]
knapsack_capacity = 10
n = len(items)

max_value = knapsack_naive(knapsack_capacity, items, n)
print(f"Maximum value that can be obtained: {max_value}")
