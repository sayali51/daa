import math
def binomial_table(n, k):
    """Return (C(n, k), table) using a full 2-D DP table."""
    if k < 0 or k > n:
        return 0, []
    # table[i][j] will hold C(i, j); only j <= min(i, k) is needed
    table = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                table[i][j] = 1                       # base cases
            else:                                     # Pascal's identity
                table[i][j] = table[i - 1][j - 1] + table[i - 1][j]
    return table[n][k], table
def binomial_optimized(n, k):
    """Return C(n, k) using a single 1-D array (space optimised)."""
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)          # C(n, k) == C(n, n-k): use the smaller k
    row = [0] * (k + 1)
    row[0] = 1                 # C(i, 0) = 1 for every i
    for i in range(1, n + 1):
        # go right-to-left so row[j-1] still holds row i-1's value
        for j in range(min(i, k), 0, -1):
            row[j] = row[j] + row[j - 1]
    return row[k]
def pascal_triangle(n):
    """Print the first n+1 rows of Pascal's triangle, built with DP."""
    rows = []
    for i in range(n + 1):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = rows[i - 1][j - 1] + rows[i - 1][j]
        rows.append(row)
    w = len(str(max(rows[-1]))) + 2          # cell width (kept even so rows
    w += w % 2                               # can be offset by half a cell)
    for i, row in enumerate(rows):
        pad = " " * ((n - i) * w // 2)
        print(pad + "".join(str(x).center(w) for x in row).rstrip())
def print_table(table, n, k):
    """Pretty-print the DP table."""
    print("\nDP table (rows = n, columns = k):")
    print("      " + "".join(f"{j:>8}" for j in range(k + 1)))
    for i in range(n + 1):
        cells = ""
        for j in range(k + 1):
            cells += f"{table[i][j]:>8}" if j <= i else " " * 8
        print(f"n={i:<3} {cells}")
def main():
    n = int(input("Enter n: "))
    k = int(input("Enter k: "))
    if n < 0 or k < 0:
        print("n and k must be non-negative integers.")
        return
    value, table = binomial_table(n, k)
    print(f"\nC({n}, {k}) using 2-D DP table      = {value}")
    print(f"C({n}, {k}) using 1-D optimised DP  = {binomial_optimized(n, k)}")
    print(f"C({n}, {k}) using math.comb (check) = {math.comb(n, k)}")
    if table and n <= 15:
        print_table(table, n, k)
    if n <= 12:
        print(f"\nPascal's triangle (rows 0 to {n}):\n")
        pascal_triangle(n)
if __name__ == "__main__":
    main()