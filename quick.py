import random
import time
import sys

sys.setrecursionlimit(10000)  # sorted input of ~5000 elements needs deep recursion


# Partition function (Lomuto partition scheme)
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Deterministic Quick Sort (pivot = last element)
def quick_sort_deterministic(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_deterministic(arr, low, pi - 1)
        quick_sort_deterministic(arr, pi + 1, high)


# Randomized partition
def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return partition(arr, low, high)


# Randomized Quick Sort
def quick_sort_randomized(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        quick_sort_randomized(arr, low, pi - 1)
        quick_sort_randomized(arr, pi + 1, high)


def timed_sort(sort_fn, data):
    arr = data.copy()
    start = time.perf_counter()
    sort_fn(arr, 0, len(arr) - 1)
    end = time.perf_counter()
    return arr, end - start


# Driver code
arr_input = list(map(int, input("Enter elements separated by space: ").split()))

if not arr_input:
    print("No elements entered.")
else:
    arr1, t1 = timed_sort(quick_sort_deterministic, arr_input)
    arr2, t2 = timed_sort(quick_sort_randomized, arr_input)

    print("\nDeterministic Quick Sort Result:", arr1)
    print(f"Execution Time: {t1:.6f} seconds")

    print("\nRandomized Quick Sort Result:", arr2)
    print(f"Execution Time: {t2:.6f} seconds")

    # Optional: benchmark on larger inputs to see the real difference
    print("\n--- Benchmark on larger inputs (n = 3000) ---")
    n = 3000
    tests = {
        "Random": [random.randint(0, 10**6) for _ in range(n)],
        "Sorted": list(range(n)),
        "Reverse sorted": list(range(n, 0, -1)),
    }
    print(f"{'Input type':<16} {'Deterministic':>15} {'Randomized':>12}")
    for name, data in tests.items():
        _, td = timed_sort(quick_sort_deterministic, data)
        _, tr = timed_sort(quick_sort_randomized, data)
        print(f"{name:<16} {td:>14.6f}s {tr:>11.6f}s")