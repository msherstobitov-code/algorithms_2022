"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы
 и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
#  сложность O(n)

def authentication_1(users, user_name, user_password):
    for key, value in users.items():
        if key == user.name:
            if value['password'] == user_password and value['activation']:
                return 'Welcome!'
            elif value['password'] == user_password and not value['activation']:
                return 'You need activation!'
            elif value['password'] != user_password:
                return 'invalid password!'
    return 'there is no such user'



#  сложность О(1)

def authentication_1(users, user_name, user_password):
    if users.get(user_name):
        if users[user_name]['password'] == user_password and users[user_name]['activation']:
            return 'Welcome'
        elif users[user_name]['password'] == user_password and not users[user_name]['activation']:
            return 'You need activation!'
        elif users[user_name]['password'] != user_password:
            return 'invalid password!'
    return 'there is no such user'