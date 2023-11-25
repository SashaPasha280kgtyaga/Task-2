def multiply_numbers(input_string):
    numbers = [float(num) for num in input_string.replace(' ', '').split(',')]
    result = 1
    for num in numbers:
        result *= num
    return result
input_numbers = "2, 3, 4, 5"
result = multiply_numbers(input_numbers)
print("Результат умножения:", result)