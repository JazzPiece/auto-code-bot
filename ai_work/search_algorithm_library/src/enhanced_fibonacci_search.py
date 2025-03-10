def fibonacci_search(arr, target):
    if not arr:
        return -1

    fib2 = 0
    fib1 = 1
    fib = fib1 + fib2

    while fib < len(arr):
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2

    offset = -1

    while fib > 1:
        i = min(offset + fib2, len(arr) - 1)

        if arr[i] < target:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif arr[i] > target:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i

    if fib1 and offset + 1 < len(arr) and arr[offset + 1] == target:
        return offset + 1

    return -1

if __name__ == "__main__":
    arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
    target = 85
    index = fibonacci_search(arr, target)
    print(f"Target found at index: {index}")