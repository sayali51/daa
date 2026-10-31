def knapsack(values, weights, capacity):
    n = len(values)

    # DP table: dp[i][w] = best value using first i items with capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build table bottom-up
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w],
                )
            else:
                dp[i][w] = dp[i - 1][w]

    max_value = dp[n][capacity]

    # Backtrack to find which items were included
    w = capacity
    items_selected = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            items_selected.append(i)      # 1-based item number
            w -= weights[i - 1]
    items_selected.reverse()

    return max_value, items_selected


# Driver code
n = int(input("Enter number of items: "))
values = []
weights = []
for i in range(n):
    v = int(input(f"Enter value of item {i + 1}: "))
    w = int(input(f"Enter weight of item {i + 1}: "))
    if w < 0:
        raise ValueError("Weight cannot be negative.")
    values.append(v)
    weights.append(w)

capacity = int(input("Enter capacity of knapsack: "))

max_value, items_selected = knapsack(values, weights, capacity)

print(f"\nMaximum value obtained: {max_value}")
print("\nItems included (1-based):")
for i in items_selected:
    print(f"Item {i}: value = {values[i - 1]}, weight = {weights[i - 1]}")
print(f"Total weight used: {sum(weights[i - 1] for i in items_selected)}")