import math

def jump_search(arr, target):
    n = len(arr)
    step = math.isqrt(n)
    prev = 0
    
    while arr[min(step, n) - 1] < target:
        prev = step
        step += math.isqrt(n)
        if prev >= n:
            return -1
    
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    
    return -1