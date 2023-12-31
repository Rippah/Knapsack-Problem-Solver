from queue import PriorityQueue

def bound(level, weight, profit, items, W):
    if weight >= W:
        return 0

    j = level + 1
    bound = profit
    total_weight = weight

    while j < len(items) and total_weight + items[j][0] <= W:
        total_weight += items[j][0]
        bound += items[j][1]
        j += 1

    if j < len(items):
        bound += (W - total_weight) * items[j][1] / items[j][0]

    return bound

def knapsack(W, items):
    items.sort(key=lambda x: x[1]/x[0], reverse=True)

    Q = PriorityQueue()
    Q.put((0, 0, 0, bound(0, 0, 0, items, W)))

    max_profit = 0

    while not Q.empty():
        level, profit, weight, _ = Q.get()

        if level < len(items):
            if weight + items[level][0] <= W:
                max_profit = max(max_profit, profit + items[level][1])
                bound_profit = bound(level, weight + items[level][0], profit + items[level][1], items, W)
                Q.put((level + 1, profit + items[level][1], weight + items[level][0], bound_profit))

            bound_profit = bound(level, weight, profit, items, W)
            if bound_profit > max_profit:
                Q.put((level + 1, profit, weight, bound_profit))

    return max_profit

items = [(2, 40), (3, 50), (2, 100), (5, 95), (3, 30)]
W = 10

print("Maximum possible profit =", knapsack(W, items))
