
import random
import time


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high, randomized=False):

    if low < high:

        # Select random pivot
        if randomized:
            p = random.randint(low, high)
            arr[p], arr[high] = arr[high], arr[p]

        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1, randomized)
        quick_sort(arr, pi + 1, high, randomized)


arr = list(map(
    int, input("Enter array elements: ").split()
))

# Deterministic Quick Sort
a = arr.copy()

start = time.perf_counter()
quick_sort(a, 0, len(a) - 1)
end = time.perf_counter()

print("Deterministic Sorted Array:", a)
print("Deterministic Time:", end - start, "seconds")


# Randomized Quick Sort
b = arr.copy()

start = time.perf_counter()
quick_sort(b, 0, len(b) - 1, True)
end = time.perf_counter()

print("Randomized Sorted Array:", b)
print("Randomized Time:", end - start, "seconds")
