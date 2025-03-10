def recursive_binary_search(arr, target, low, high):
    if low > high:
        return -1

    mid = low + (high - low) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, high)
    else:
        return recursive_binary_search(arr, target, low, mid - 1)

def recursive_ternary_search(arr, target, low, high):
    if low > high:
        return -1

    mid1 = low + (high - low) // 3
    mid2 = high - (high - low) // 3

    if arr[mid1] == target:
        return mid1
    if arr[mid2] == target:
        return mid2

    if target < arr[mid1]:
        return recursive_ternary_search(arr, target, low, mid1 - 1)
    elif target > arr[mid2]:
        return recursive_ternary_search(arr, target, mid2 + 1, high)
    else:
        return recursive_ternary_search(arr, target, mid1 + 1, mid2 - 1)