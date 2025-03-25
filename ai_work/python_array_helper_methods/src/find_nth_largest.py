def find_nth_largest(arr, n):
    sorted_arr = sorted(arr, reverse=True)
    if n <= len(sorted_arr):
        return sorted_arr[n-1]
    else:
        return "Invalid input"