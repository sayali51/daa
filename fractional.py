# Function to solve fractional knapsack
def fractional_knapsack(values, weights, capacity):
    n = len(values)

    # (ratio, weight, value); zero-weight items get infinite ratio so they're taken first
    items = []
    for i in range(n):
        if weights[i] == 0:
            ratio = float("inf")
        else:
            ratio = values[i] / weights[i]
        items.append((ratio, weights[i], values[i]))

    # Sort by ratio in descending order
    items.sort(key=lambda x: x[0], reverse=True)

    total_value = 0.0
    fractions = []

    for ratio, w, v in items:
        if capacity <= 0:
            break
        if w <= capacity:
            # Take the whole item
            total_value += v
            capacity -= w
            fractions.append((v, w, 1.0))
        else:
            # Take a fraction of the item
            fraction = capacity / w
            total_value += v * fraction
            fractions.append((v, w, fraction))
            capacity = 0
            break

    return total_value, fractions


# Driver code
n = int(input("Enter number of items: "))
values = []
weights = []
for i in range(n):
    v = float(input(f"Enter value of item {i + 1}: "))
    w = float(input(f"Enter weight of item {i + 1}: "))
    values.append(v)
    weights.append(w)

capacity = float(input("Enter capacity of knapsack: "))

max_value, fractions_taken = fractional_knapsack(values, weights, capacity)

print(f"\nMaximum value obtained: {max_value:.2f}")
print("\nItems taken:")
print(f"{'Value':>10} {'Weight':>10} {'Fraction':>10}")
for v, w, f in fractions_taken:
    print(f"{v:>10.2f} {w:>10.2f} {f:>10.2f}")