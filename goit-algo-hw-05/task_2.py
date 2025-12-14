def binary_search_upper_bound(arr, target):
    left = 0
    right = len(arr) - 1
    iterations = 0
    result_index = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] >= target:
            result_index = mid
            right = mid - 1
        else:
            left = mid + 1

    if result_index is None:
        return iterations, None
    else:
        return iterations, arr[result_index]

arr = [1.1, 1.7, 2.2, 2.5, 3.3, 4.0, 4.2, 5.0, 5.7, 6.0]
result = binary_search_upper_bound(arr, 2.0)
print(result)