def divide_numbers(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero"

result = divide_numbers(10, 2)
print(result)