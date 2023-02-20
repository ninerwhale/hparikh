def get_unique_list(my_list):
    return list(set(my_list))

my_list = [1, 2, 3, 2, 1, 4]
unique_list = get_unique_list(my_list)
print(unique_list)