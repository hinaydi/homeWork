# # 1. Напишите функцию get_multiplied_digits и параметр number в ней
# def get_multiplied_digits(number):
#     # 2. Создайте переменную str_number и запишите строковое представление(str) числа number в неё.
#     str_number = str(number)
#     # 3. создайте переменную first и запишите в неё первый символ из str_number в числовом представлении(int).
#     first = int(str_number[0])
#     # 5. пункт можно выполнить только тогда, когда длина str_number больше 1, т.к.
#     # в противном случае не получиться взять срез str_number[1:].
#     if len(str_number) > 1:
#         # 4. Возвращайте значение first * get_multiplied_digits(int(str_number[1:]))
#         return first * get_multiplied_digits(int(str_number[1:]))
#     else:
#         # 6. Если же длина str_number не больше 1, тогда вернуть оставшуюся цифру first.
#         return int(str_number)
#
#
# result = get_multiplied_digits(40203)
# print(result)


def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) >= 2:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return int(str_number)


result = get_multiplied_digits(40203)
print(result)