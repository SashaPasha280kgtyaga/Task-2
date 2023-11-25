def is_increasing(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] <= numbers[i - 1]:
            return False
    return True

array1 = [1, 2, 3, 4, 5]
array2 = [1, 2, 2, 4, 5]

print(is_increasing(array1))
print(is_increasing(array2))