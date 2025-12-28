import timeit

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key
    return lst

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    return merged

def timsort(lst):
    return sorted(lst)

def measure(func, data):
    return min(timeit.repeat(lambda: func(data[:]), repeat=5, number=1))

data_random = [5, 3, 8, 4, 2, 9, 1, 7, 6] * 300
data_reversed = list(range(3000, 0, -1))
data_sorted = list(range(3000))

print("DATASET: random")
print("Insertion:", measure(insertion_sort, data_random))
print("Merge:    ", measure(merge_sort, data_random))
print("Timsort:  ", measure(timsort, data_random))

print("\nDATASET: reversed")
print("Insertion:", measure(insertion_sort, data_reversed))
print("Merge:    ", measure(merge_sort, data_reversed))
print("Timsort:  ", measure(timsort, data_reversed))

print("\nDATASET: sorted")
print("Insertion:", measure(insertion_sort, data_sorted))
print("Merge:    ", measure(merge_sort, data_sorted))
print("Timsort:  ", measure(timsort, data_sorted))
