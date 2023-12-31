def knapsack_greedy(W, items):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    remain = W
    result = 0
    i = 0

    while i < len(items):
        if items[i][0] <= remain:
            remain -= items[i][0]
            result += items[i][1]

            print("Pack", i, "- Weight", items[i][0], "- Value", items[i][1])

        i += 1

    print("Max Value:", result)

items = [(2, 40), (3, 50), (2, 100), (5, 95), (3, 30)]
W = 10

knapsack_greedy(W, items)

