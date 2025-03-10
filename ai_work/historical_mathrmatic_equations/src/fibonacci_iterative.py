def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    
    return fib_series[n-1]

# Example usage
print(fibonacci(6))  # 5