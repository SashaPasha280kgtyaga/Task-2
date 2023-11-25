def button_press(message):
    button_presses = ""
    for char in message:
        if char.lower() == 'a':
            button_presses += '1'
        elif char.lower() == 'e':
            button_presses += '55555'
        elif char.lower() == 'g':
            button_presses += '7777777'
        else:
            pass
    return button_presses

message = "AEG"
result = button_press(message)
print(result)