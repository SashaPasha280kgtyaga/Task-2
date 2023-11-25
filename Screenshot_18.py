def cumulative_sum(input_list):
    result_list = []
    current_sum = 0

    for number in input_list:
        current_sum += number
        result_list.append(current_sum)

    return result_list

input_numbers = [1, 2, 3, 4, 5]
result = cumulative_sum(input_numbers)
print(result)