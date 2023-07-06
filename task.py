import string
import pandas as pd

df = pd.read_csv("data.csv", sep=',')


def available(symb=''):
    """Всі доступні символи"""
    cyrillic = ''
    for l in range(ord('а'), ord('я') + 1): # не маштабовано
        letter = chr(l)
        cyrillic += letter
    letters = string.ascii_letters + cyrillic + "!" + "'"
    if symb:
        letters += symb
    return letters

def invalid(symb=''):
    """Всі недоступні символи"""
    letters = '"@#$%^&*'
    if symb:
        letters += symb
    return letters


def check(string, invalid, available):
    """Перевіряє рядки"""
    for i in string:
        if i not in available or i in invalid:
            return True
    return False


def start(data, add_av='', add_inv=''):
    invalid_rows = []    # Список в якому зберігаються всі неправильні рядки
    if add_av or add_inv:   # Якщо були передані додаткові символи (add_inv - недоступні,
        x = available(add_av)   # add_av - доступні), то викликається спеціальна функція(-ії),
        y = invalid(add_inv)    # яка додає символ(-и) до списку доступності/недоступності
    else:
        x = available()
        y = invalid()

    for index, row in data.iterrows():
        firstname = row['FirstName']
        lastname = row['LastName']
        middlename = row['MiddleName']

        # Запускажмо функцію check, якщо були знайдені недоступні символи, то програма додає ці
        # рядки до спсику invalid_rows
        if check(firstname, y, x)\
                or check(lastname, y, x)\
                or check(middlename, y, x):
            invalid_rows.append(row)

    return invalid_rows


x = start(df)
print(x)




