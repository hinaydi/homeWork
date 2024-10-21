# закрепить знание использования параметров *args/ **kwargs на практике


# Задача "Однокоренные":
# Напишите функцию single_root_words, которая принимает одно обязательное слово
# в параметр root_word, а далее неограниченную последовательность в параметр *other_words.
# Функция должна составить новый список same_words только из тех слов списка other_words,
# которые содержат root_word или наоборот root_word содержит одно из этих слов.
# После вернуть список same_words в качестве результата своей работы.

# 1. Объявите функцию single_root_words и напишите в ней параметры root_word и *other_words.
def single_root_words(root_word, *other_words):
    # 2. Создайте внутри функции пустой список same_words, который пополнится нужными словами.
    same_words = []  # пустой список
    # 3. При помощи цикла for переберите предполагаемо подходящие слова.
    for i in other_words:
        other_words = i.lower()  # преобразование регистра и изменение имени переменной
        root_word = root_word.lower()  # преобразование регистра
        if root_word in other_words or other_words in root_word:
            # 4. Пропишите корректное относительно задачи условие, при котором
            # добавляются слова в результирующий список same_words.
            same_words.append(i)
    # 5. После цикла верните образованный функцией список same_words.

    return same_words


# 6. Вызовите функцию single_root_words
# и выведете на экран(консоль) возвращённое ей значение.

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
