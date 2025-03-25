def array_statistics(arr):
    total_elements = len(arr)
    sum_elements = sum(arr)
    mean = sum_elements / total_elements
    max_value = max(arr)
    min_value = min(arr)
    return total_elements, sum_elements, mean, max_value, min_value