def find_median(arr):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    if n % 2 == 0:
        return (sorted_arr[n//2 - 1] + sorted_arr[n//2]) / 2
    else:
        return sorted_arr[n//2]