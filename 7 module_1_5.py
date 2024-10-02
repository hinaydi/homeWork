immutable_tuple = 1, 2, 'load', 'Boot'
print(immutable_tuple)
# immutable_var[1] = 5
# print(immutable_var)
# ошибка, tuple не любит изменение элементов
mutable_list = 'ace', [1, 2, 4], [6, 7, 8], 'one', 'two'
mutable_list[2][2] = 777
mutable_list[1][2] = 'live'
print(mutable_list)