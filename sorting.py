import time
import random


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    data_size = 10000
    test_data = [random.randint(0, 100000) for _ in range(data_size)]

    print(f"Сортування {data_size} елементів...")

    start = time.time()
    merge_sort(test_data.copy())
    print(f"MergeSort: {time.time() - start:.4f} сек")

    start = time.time()
    quick_sort(test_data.copy())
    print(f"QuickSort: {time.time() - start:.4f} сек")