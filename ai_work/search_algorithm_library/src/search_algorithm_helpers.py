import math

def jump_search(arr, target):
    n = len(arr)
    step = math.isqrt(n)
    prev = 0

    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += math.isqrt(n)
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i

    return -1

def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] != arr[high]:
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    if low <= high and arr[low] == target:
        return low

    return -1

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1