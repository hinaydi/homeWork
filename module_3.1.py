# Счётчик вызовов
# Создаем переменную calls = 0 вне функций
calls = 0


# Функция count_calls подсчитывающая вызовы остальных функций.

# Создать функцию count_calls
# и изменять в ней значение переменной calls

def count_calls():
    # изменяем значение переменной calls ключевым словом Global
    global calls
    calls += 1


# Функция is_contains принимает два аргумента: строку и список, и
# возвращает True, если строка находится в этом списке,
# False - если отсутствует. Регистром строки при проверке пренебречь.

# Создать функцию string_info с параметром string
# и реализовать логику работы по описанию
# Функция string_info принимает аргумент - строку
# и возвращает кортеж из: длины этой строки,
# строку в верхнем регистре, строку в нижнем регистре

def string_info(string):
    count_calls()
    return (len(string),  # длины строки
            string.upper(),  # строку в верхнем регистре
            string.lower())  # строку в нижнем регистре


# Функция string_info принимает аргумент - строку и возвращает кортеж из:
# длины этой строки, строку в верхнем регистре, строку в нижнем регистре.

# Создать функцию is_contains с двумя параметрами string и list_to_search
# Функция is_contains принимает два аргумента: строку и список,
# и возвращает True, если строка находится в этом списке,
# False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN

def is_contains(string, list_to_search):
    count_calls()
    # Функция any проверяет элементы в последовательности.
    # Если хотя бы один из элементов является истинным,
    # он вернет нам True, в противном случае, мы получим False.
    return any(string.upper() in i.upper() for i in list_to_search)


print(string_info('Capybara'))
print(string_info('mozgolom'))
print(string_info('life is good'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(is_contains('micky', ['mIc', 'mY', 'My']))
print(is_contains('micky', ['mic', 'MiCky', 'mICKy']))
print(calls)
