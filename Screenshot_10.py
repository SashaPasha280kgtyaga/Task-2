def coordinates_to_array(x_list, y_list):
    result = []
    for i in range(len(x_list)):
        result.append([x_list[i], y_list[i]])
    return result

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]

result = coordinates_to_array(x, y)

print(result)
