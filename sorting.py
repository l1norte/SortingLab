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


def run_demonstration():
    data_20 = [random.randint(1, 99) for _ in range(20)]

    print("Вимога: 20 випадкових значень")
    print("MergeSort до:   ", *data_20)
    print("MergeSort після:", *merge_sort(data_20.copy()))

    print("\nQuickSort до:   ", *data_20)
    print("QuickSort після:", *quick_sort(data_20.copy()))

    print("\nВимога: замір часу для 10 000 елементів")
    data_10k = [random.randint(0, 100000) for _ in range(10000)]

    start = time.time()
    merge_sort(data_10k.copy())
    print(f"MergeSort: {time.time() - start:.4f} сек")

    start = time.time()
    quick_sort(data_10k.copy())
    print(f"QuickSort: {time.time() - start:.4f} сек")


if __name__ == "__main__":
    run_demonstration()