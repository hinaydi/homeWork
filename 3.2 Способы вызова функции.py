# Создайте функцию, которая принимает 2 обычных и 1 именованный аргумент со значением по умолчанию
# message(сообщение), recipient(получатель), sender(отправитель)
# Обязательно именованные аргументы отделяются от остальных символом "*" перед ними

def send_email(massege, recipient, *, sender="University.help@gmail.com"):
    # Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net",
    # то вывести на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
    #
    # Метод endswith() возвращает True, если строка заканчивается указанным суффиксом. Если нет, возвращается False.
    # Синтаксис метода: str.endswith(suffix[, start[, end]]).
    # Метод endswith принимает три параметра:
    # suffix — строка или кортеж суффиксов для проверки;
    # start (необязательно) — начальная позиция, в которой следует проверить суффикс в строке.
    # end (необязательно) — конечная позиция, в которой следует проверить суффикс в строке.

    if '@' not in recipient or not recipient.endswith \
                (('.com', '.ru', '.net')) or '@' not in sender or not sender.endswith(('.com', '.ru', '.net')):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

    # Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
    elif recipient == sender:
        print(f"Нельзя отправить письмо самому себе!")

    # Если же отправитель по умолчанию - university.help@gmail.com,
    # то вывести сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
    elif sender == "University.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")

    # В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!
    # Письмо отправлено с адреса <sender> на адрес <recipient>."
    elif sender != "University.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


# Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com
send_email('messege', 'vasyok1337@gmail.com')
# НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru
send_email('messege', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
# Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru
send_email('messege', 'urban.teacher@mail.uk', sender='urban.teacher@mail.uk')
# Нельзя отправить письмо самому себе!
send_email('messege', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

# send_email('Это сообщение для проверки связи',
#            'vasyok1337@gmail.com')
# send_email('Вы видите это сообщение как лучший студент курса!',
#            'urban.fan@mail.ru', sender='urban.info@gmail.com')
# send_email('Пожалуйста, исправьте задание',
#            'urban.teacher@mail.uk', sender='urban.teacher@mail.uk')
# send_email('Напоминаю самому себе о вебинаре',
#            'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
