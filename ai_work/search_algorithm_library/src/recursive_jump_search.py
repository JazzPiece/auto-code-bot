import math

def recursive_jump_search(arr, target, prev, step):
    if prev >= len(arr):
        return -1

    if arr[min(step, len(arr)) - 1] >= target:
        for i in range(prev, min(step, len(arr))):
            if arr[i] == target:
                return i
        return -1

    return recursive_jump_search(arr, target, step, step + math.isqrt(len(arr)))

def jump_search_recursive(arr, target):
    step = math.isqrt(len(arr))
    return recursive_jump_search(arr, target, 0, step)

if __name__ == "__main__":
    arr = [0, 1, 22, 35, 40, 41, 45, 54, 60, 70]
    target = 45
    index = jump_search_recursive(arr, target)
    print(f"Target found at index: {index}")