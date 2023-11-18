def remove_extra_spaces(input_string):
    words = input_string.split()
    result_string = ' '.join(words)
    return result_string
input_str = "   Это   строка   с   лишними   пробелами.   "
output_str = remove_extra_spaces(input_str)
print(output_str)