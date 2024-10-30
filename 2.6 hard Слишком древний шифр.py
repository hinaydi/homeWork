def find_password(n):
    result = ""
    for i in range(1, n):
        # print(i)
        for j in range(i + 1, n):
            if i + j <= n and n % (i + j) == 0:
                result += f"{i}{j}"
    return result


n = int(input('Введите число от 3 до 20:  '))
result = find_password(n)
print('Пароль: ', result)