def has_duplicate_letters(word):
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            return True
    return False
word = "hello"
result = has_duplicate_letters(word)
print(result)