def remove_enemy_names(names, enemies):
    filtered_names = [name for name in names if name not in enemies]
    return filtered_names

all_names = ["Alice", "Bob", "Charlie", "David"]
enemies_list = ["Bob", "David"]

filtered_names = remove_enemy_names(all_names, enemies_list)
print(filtered_names)