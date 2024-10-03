# Словарь
my_dict = {'home': 135, 'street': 455, 'sity': 680000}
print('Мой словарь:', my_dict)
print('Значение ключа sity', my_dict['sity'])
print(my_dict.get('Venera', 'нет такого ключа'))
my_dict.update({'luna': 385000, 'mars': 4})
rem = my_dict.pop('street')
print('Значение удаленного ключа', rem)
print('Измененный словарь:', my_dict)

# Множества
my_set = {1, 2, 3, 2, 4, 4, 5, True, 'list', 'map'}
my_set.add('hope'),
my_set.add(8)
print('Множество:', my_set)
my_set.discard('list')
print('Измененное множество:', my_set)
