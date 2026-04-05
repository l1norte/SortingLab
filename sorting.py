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


def run_lab_requirements():
    print("=== ЗАМІР ЧАСУ: 10 000 елементів ===")
    data_10k = [random.randint(0, 100000) for _ in range(10000)]

    s1 = time.time()
    merge_sort(data_10k.copy())
    print(f"MergeSort (10k): {time.time() - s1:.4f} сек")

    s2 = time.time()
    quick_sort(data_10k.copy())
    print(f"QuickSort (10k): {time.time() - s2:.4f} сек")

    print("\n=== РЕЗУЛЬТАТИ: 20 000 елементів ===")
    data_20k = [random.randint(1, 1000000) for _ in range(20000)]

    print("До сортування (перші 20):")
    print(*(data_20k[:20]))

    s3 = time.time()
    sorted_m = merge_sort(data_20k.copy())
    print("Після MergeSort (перші 20):")
    print(*(sorted_m[:20]))
    print(f"Час MergeSort (20k): {time.time() - s3:.4f} сек")

    s4 = time.time()
    sorted_q = quick_sort(data_20k.copy())
    print("Після QuickSort (перші 20):")
    print(*(sorted_q[:20]))
    print(f"Час QuickSort (20k): {time.time() - s4:.4f} сек")


if __name__ == "__main__":
    run_lab_requirements()